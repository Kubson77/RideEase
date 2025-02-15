from datetime import date

import uvicorn
from fastapi import FastAPI, HTTPException, Query
from sqlalchemy import select

from sqlmodels.car import Car
from sqlmodels.customer import Customer
from sqlmodels.first_name import FirstName
from sqlmodels.last_name import LastName
from sqlmodels.rent_car import RentCar
from utils.connection import db_dependency

app = FastAPI()


# Endpoint to list rented cars
@app.get("/rented_cars/")
def list_rented_cars(db: db_dependency):
    rented_cars = (
        db.query(RentCar)
        .join(Car)
        .join(Customer)
        .filter(RentCar.returned_on.is_(None))
        .all()
    )

    return [
        {
            "plate_number": rent.car.plate_number,
            "brand": rent.car.brand.name,
            "model": rent.car.model.name,
            "customer": f"{rent.customer.first_name.name} {rent.customer.last_name.name}",
            "rented_on": rent.rented_on.strftime("%Y-%m-%d"),
        }
        for rent in rented_cars
    ]


# Endpoint to list available cars
@app.get("/available_cars/")
def list_available_cars(db: db_dependency):
    subquery = select(RentCar.car_id).where(RentCar.returned_on < date.today())

    available_cars = db.query(Car).filter(Car.id.in_(subquery.distinct())).all()

    return [
        {
            "plate_number": car.plate_number,
            "brand": car.brand.name,
            "model": car.model.name,
        }
        for car in available_cars
    ]


@app.post("/rent_car/")
def rent_car(
    db: db_dependency,
    licence_number: str = Query(..., min_length=5, max_length=20),
    first_name: str = None,
    last_name: str = None,
):
    customer = (
        db.query(Customer).filter(Customer.licence_number == licence_number).first()
    )

    if not customer:
        if not first_name or not last_name:
            raise HTTPException(
                status_code=400,
                detail="Customer not found. For registering provide first name and last name",
            )

        first_name_obj = (
            db.query(FirstName).filter(FirstName.name == first_name).first()
        )
        if not first_name_obj:
            first_name_obj = FirstName(name=first_name)
            db.add(first_name_obj)
            db.commit()
            db.refresh(first_name_obj)

        last_name_obj = db.query(LastName).filter(LastName.name == last_name).first()
        if not last_name_obj:
            last_name_obj = LastName(name=last_name)
            db.add(last_name_obj)
            db.commit()
            db.refresh(last_name_obj)

        customer = Customer(
            first_name_id=first_name_obj.id,
            last_name_id=last_name_obj.id,
            licence_number=licence_number,
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)

    subquery = db.query(RentCar.car_id).filter(RentCar.returned_on.is_(None)).subquery()

    available_car = db.query(Car).filter(~Car.id.in_(subquery)).first()

    if not available_car:
        raise HTTPException(status_code=400, detail="No cars available.")

    rent_entry = RentCar(
        car_id=available_car.id, customer_id=customer.id, rented_on=date.today()
    )
    db.add(rent_entry)
    db.commit()

    return {
        "message": f"Car rented successfully by customer: {customer.first_name} {customer.last_name}",
        "customer": f"{customer.first_name.name} {customer.last_name.name}",
        "plate_number": available_car.plate_number,
        "brand": available_car.brand.name,
        "model": available_car.model.name,
        "rented_on": date.today().strftime("%Y-%m-%d"),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
