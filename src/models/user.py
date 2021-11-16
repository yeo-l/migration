from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from ..config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String(255))
    email = Column('email', String(255))
    password = Column('password', String(255))
