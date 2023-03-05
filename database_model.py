import datetime

from constants import info_categories, fin_categories, dict_periods
import sqlalchemy
from sqlalchemy import create_engine, select
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///koyfindb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class KoyfinWarehouse(Base):
    __tablename__ = "KoyfinFinData"
    id = Column("id", Integer, primary_key=True)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


# add keys from info categories to database
for key in info_categories.keys():
    setattr(KoyfinWarehouse, key, Column(str(key), String, default=10))

# add periods for each fin category to database
for fin_cat in fin_categories:
    temp_list = [fin_cat[0] + dict_period for dict_period in dict_periods.keys()]
    for period in temp_list:
        setattr(KoyfinWarehouse, period, Column(str(period), Integer, default=10))

# add date of addition to database
setattr(KoyfinWarehouse, "date", Column("date", DateTime, default=datetime.datetime.utcnow()))

Base.metadata.create_all(bind=engine)

