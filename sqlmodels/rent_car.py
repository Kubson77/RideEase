from sqlalchemy import DATE, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from sqlmodels.base_model import BaseModel
from sqlmodels.car import Car
from sqlmodels.customer import Customer


class RentCar(BaseModel):
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    rented_on = Column(DATE, nullable=False)
    returned_on = Column(DATE, nullable=True)

    # relationships
    car = relationship(Car, backref="car_rents")
    customer = relationship(Customer, backref="car_rents")

    def __str__(self):
        return f"{self.car} {self.customer}"
