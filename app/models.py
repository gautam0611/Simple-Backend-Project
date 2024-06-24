"""
This file contains the sql alchemy models
"""
from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Item(Base):
    __tablename__="items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    description = Column(Text)



