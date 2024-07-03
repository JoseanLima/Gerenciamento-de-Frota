from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Manutencao(Base):
    __tablename__ = 'manutencao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    custo = Column(Float)
    veiculo_id = Column(Integer, ForeignKey('motoristas.id'))  # Corrigido para referenciar motoristas.id

    def __repr__(self):
        return f"<Manutencao(id={self.id}, descricao={self.descricao}, custo={self.custo}, veiculo_id={self.veiculo_id})>"
