#!/usr/bin/python3
'''
a python file that contains the class definition of a State 
'''
from sqlalchemy import (create_engine, ForeignKey,
                        String, Integer, Column, CHAR)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class States(Base):
    '''
    Script to list all cities of a specified state from a MySQL database.
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)