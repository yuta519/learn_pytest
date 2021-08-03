from sqlalchemy import (Table, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(20), index=True)
    user_age = Column(Integer())