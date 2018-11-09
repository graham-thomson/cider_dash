from sqlalchemy import Column, Integer, DateTime, Numeric
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EnvTemps(Base):
    __tablename__ = 'envtemps'

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, nullable=False)
    sh_temp = Column(Numeric, nullable=True)
    adj_sh_temp = Column(Numeric, nullable=True)
    local_outdoor_temp = Column(Numeric, nullable=True)
    cpu_temp = Column(Numeric, nullable=True)

engine = create_engine('sqlite:///temps.db')
Base.metadata.create_all(engine)