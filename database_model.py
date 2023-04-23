import datetime
from constants import INFO_CATEGORIES, FIN_CATEGORIES, DICT_PERIODS
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
for key in INFO_CATEGORIES.keys():
    setattr(KoyfinWarehouse, key, Column(str(key), String, default=10))

# add periods for each fin category to database
for fin_cat in FIN_CATEGORIES:
    temp_list = [fin_cat[0] + dict_period for dict_period in DICT_PERIODS.keys()]
    for period in temp_list:
        setattr(KoyfinWarehouse, period, Column(str(period), Integer, default=10))

# add date of addition to database
setattr(KoyfinWarehouse, "date", Column("date", DateTime, default=datetime.datetime.utcnow()))
# add setatr for update cause
setattr(KoyfinWarehouse, "financial_data_update_date", Column("financial_data_update_date", DateTime))

Base.metadata.create_all(bind=engine)


def add_new_company_data(**kwargs):
    """add new company record to database if record doesn't exist"""
    exist = session.query(KoyfinWarehouse).filter(KoyfinWarehouse.name == kwargs['name']).all()
    if len(exist) > 0:
        print(kwargs['name'], "Record exists")
    else:
        record = KoyfinWarehouse(**kwargs)
        print(record)
        session.add(record)
        session.commit()


def update_company_data(**kwargs):
    """update company record with new data"""
    record = session.execute(select(KoyfinWarehouse).filter_by(name=str(kwargs["name"]))).scalar_one()
    if record.cur_evebitda != kwargs['cur_evebitda'] or record.cur_pe != kwargs['cur_pe'] or \
            record.forward_pe != kwargs['forward_pe']:
        record.cur_evebitda = kwargs['cur_evebitda']
        record.cur_pe = kwargs['cur_pe']
        record.forward_pe = kwargs['forward_pe']

    print(type(record.reve_curr), type(kwargs['reve_curr']))
    print(type(record.gm_curr), type(kwargs['gm_curr']))
    print(type(record.ebitda_curr), type(kwargs['ebitda_curr']))
    print(type(record.ni_curr), type(kwargs['ni_curr']))

    if float(record.reve_curr) != float(kwargs['reve_curr']) or float(record.gm_curr) != float(kwargs['gm_curr']) or \
            float(record.ebitda_curr) != float(kwargs['ebitda_curr']) or float(record.ni_curr) != float(kwargs['ni_curr']):
        for cat in FIN_CATEGORIES:
            for key, value in DICT_PERIODS.items():
                setattr(record, cat[0] + key, kwargs[cat[0] + key])
        record.financial_data_update_date = datetime.datetime.utcnow()
        print("Financial data updated")

    session.add(record)
    session.commit()

