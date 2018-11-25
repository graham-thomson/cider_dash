import time
import datetime as dt
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sense_hat import SenseHat

from mercury.tables import Base, EnvTemps
from mercury.measures import *


def insert_envtemp_data(base, datetime, sh_temp, adj_sh_temp, local_outdoor_temp, cpu_temp):
    engine = create_engine('sqlite:///temps.db')
    base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    new_temps = EnvTemps(
        datetime=datetime,
        sh_temp=sh_temp,
        adj_sh_temp=adj_sh_temp,
        local_outdoor_temp=local_outdoor_temp,
        cpu_temp=cpu_temp)

    session.add(new_temps)
    session.commit()


def create_mock_data():
    insert_envtemp_data(Base,
                        dt.datetime.now(),
                        random.randint(0, 100),
                        random.randint(0, 100),
                        random.randint(0, 100),
                        random.randint(0, 100)
                        )

def get_current_conditions():
    sense = SenseHat()

    insert_envtemp_data(Base,
                        dt.datetime.now(),
                        float(get_inside_temp(sense)),
                        float(calibrated_temp(sense)),
                        get_outside_temp("7c5e200a31d7dcd5e40cbbf4de0f37e7", 42.3566424, -71.0644743),
                        float(cpu_temp())
                        )