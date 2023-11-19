#!/usr/bin/python3
'''
Improve the files  model_state.py
'''
from sqlalchemy import (create_engine, ForeignKey,
                        String, Integer, Column, CHAR)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

class State(Base):
    '''
    Script to list all cities of a specified state from a MySQL database.
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")