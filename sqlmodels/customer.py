from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlmodels.base_model import BaseModel
from sqlmodels.first_name import FirstName
from sqlmodels.last_name import LastName


class Customer(BaseModel):
    first_name_id = Column(
        "first_name", Integer, ForeignKey("first_name.id"), nullable=False
    )
    last_name_id = Column(
        "last_name", Integer, ForeignKey("last_name.id"), nullable=False
    )
    licence_number = Column(String(20), nullable=True)

    # relationships
    first_name = relationship(FirstName, backref="customers")
    last_name = relationship(LastName, backref="customers")

    def __str__(self):
        return f"{self.first_name.name} {self.last_name.name}"
