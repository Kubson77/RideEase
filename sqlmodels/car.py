from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlmodels.base_model import BaseModel
from sqlmodels.car_brand import CarBrand
from sqlmodels.car_model import CarModel


class Car(BaseModel):
    brand_id = Column(Integer, ForeignKey("car_brand.id"), nullable=False)
    model_id = Column(Integer, ForeignKey("car_model.id"), nullable=False)
    plate_number = Column(String(10), nullable=False)

    # relationships
    brand = relationship(CarBrand, backref="cars")
    model = relationship(CarModel, backref="cars")

    def __str__(self):
        return f"{self.brand.name} {self.model.name}"
