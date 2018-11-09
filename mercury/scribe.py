import os
import pandas as pd
import sqlite3
from sqlalchemy import engine

import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class EnvTemps(Base):
    __tablename__ = 'env_temps'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    datetime = Column(DateTime, nullable=False)
    sh_temp = Column(Numeric, nullable=True)
    adj_sh_temp = Column(Numeric, nullable=True)
    name = Column(String(250), nullable=False)


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

def create_tables():
    pass

if __name__ == '__main__':

    if not os.path.isfile("temps.db"):
        # create database and tables
        create_tables()
        pass
