from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URI = 'mysql+mysqlconnector://root:flamengo.19@localhost:3306/GerenciamentoFrota'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Veiculo(Base):
    __tablename__ = 'veiculo'
    id = Column(Integer, primary_key=True)
    placa = Column(String(7))
    modelo = Column(String(50))
    ano = Column(String(4))

class Manutencao(Base):
    __tablename__ = 'manutencao'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(255))
    data = Column(String(10))
    veiculo_id = Column(Integer, ForeignKey('veiculo.id'))

class Rota(Base):
    __tablename__ = 'rota'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(255))
    veiculo_id = Column(Integer, ForeignKey('veiculo.id'))

Base.metadata.create_all(engine)
