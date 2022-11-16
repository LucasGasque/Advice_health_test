from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, String, Boolean, Integer

from app.configs.database import db


@dataclass
class CarOwner(db.Model):
    id: int
    name: str
    sale_opportunity: bool
    cars: list

    __tablename__ = "car_owners"

    id = Column(
        Integer,
        ForeignKey("auths.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    )
    sale_opportunity = Column(Boolean, default=False)
    name = Column(String(100), nullable=False)

    auth = db.relationship(
        "Auth", backref=db.backref("user", uselist=False, cascade="all,delete")
    )

    cars = db.relationship(
        "Car", backref=db.backref("car_owner", uselist=True, cascade="all,delete")
    )
