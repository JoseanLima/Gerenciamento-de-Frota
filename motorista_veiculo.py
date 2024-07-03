from sqlalchemy import Column, Integer, String, Float
from database import Base

class MotoristaVeiculo(Base):
    __tablename__ = 'motoristas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    cpf = Column(String(14), unique=True)
    quilometragem = Column(Float)
    consumo = Column(Float)
    marca = Column(String(50))
    placa = Column(String(10))
    quilometragemRodada = Column(Float)  

    def __init__(self, nome, cpf, quilometragem, consumo, marca, placa, quilometragemRodada):
        self.nome = nome
        self.cpf = cpf
        self.quilometragem = quilometragem
        self.consumo = consumo
        self.marca = marca
        self.placa = placa
        self.quilometragemRodada = quilometragemRodada 
