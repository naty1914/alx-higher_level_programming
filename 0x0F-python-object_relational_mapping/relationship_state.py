#!/usr/bin/python3
""" A module that defines a State class that inheritesfrom an instance of
declarative_base
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

custom_metadata = MetaData()
Base = declarative_base(metadata=custom_metadata)


class State(Base):
    """ A class representin a state with id, name,cities attribute"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
