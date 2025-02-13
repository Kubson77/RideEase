from sqlalchemy import Column, String

from sqlmodels.base_model import BaseModel


class CarModel(BaseModel):
    name = Column(String(15), nullable=False)

    def __str__(self):
        return self.name
