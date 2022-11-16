from dataclasses import dataclass

from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ENUM, UUID

from app.configs.database import db


@dataclass
class Car(db.Model):

    id: int
    name: str
    color: str
    model: str

    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    color = Column(ENUM("yellow", "blue", "gray", name="Color"), nullable=False)
    model = Column(ENUM("hatch", "sedan", "convertible", name="Model"), nullable=False)
    car_owner_id = Column(
        Integer,
        ForeignKey("car_owners.id", ondelete="CASCADE"),
        nullable=False,
    )
