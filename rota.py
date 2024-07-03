from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Rota(Base):
    __tablename__ = 'rota'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    motorista_id = Column(Integer, ForeignKey('motoristas.id'))  # Ajuste na referência da chave estrangeira

    def __repr__(self):
        return f"<Rota(id={self.id}, descricao={self.descricao}, motorista_id={self.motorista_id})>"
