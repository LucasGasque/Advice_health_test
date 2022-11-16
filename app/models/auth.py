from dataclasses import dataclass
from uuid import uuid4

from sqlalchemy import Column, String, Integer
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class Auth(db.Model):
    id: int

    __tablename__ = "auths"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(124), nullable=False, unique=True)
    password_hash = Column(String(511), nullable=False)

    @property
    def password(self):
        raise AttributeError("Not allowed to access password")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
