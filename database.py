from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+pymysql://root:flamengo.19@3306/GerenciamentoFrota'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
