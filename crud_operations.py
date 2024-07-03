from database import Session
from motorista_veiculo import MotoristaVeiculo
from manutencao import Manutencao
from rota import Rota

def add_motorista(nome, cpf, quilometragem, quilometragemRodada, consumo, marca, placa):
    session = Session()
    motorista = MotoristaVeiculo(
        nome=nome,
        cpf=cpf,
        quilometragem=quilometragem,
        quilometragemRodada=quilometragemRodada,
        consumo=consumo,
        marca=marca,
        placa=placa
    )
    session.add(motorista)
    session.commit()
    session.close()

def get_motorista(id_funcionario):
    session = Session()
    motorista = session.query(MotoristaVeiculo).get(id_funcionario)
    session.close()
    return motorista

def update_motorista(id_funcionario, **kwargs):
    session = Session()
    motorista = session.query(MotoristaVeiculo).get(id_funcionario)
    if motorista:
        for key, value in kwargs.items():
            setattr(motorista, key, value)
        session.commit()
    session.close()

def delete_motorista(id_funcionario):
    session = Session()
    motorista = session.query(MotoristaVeiculo).get(id_funcionario)
    if motorista:
        session.delete(motorista)
        session.commit()
    session.close()

def list_motoristas():
    session = Session()
    motoristas = session.query(MotoristaVeiculo).all()
    session.close()
    return motoristas

# Funções para Manutencao
def agendar_manutencao(id_funcionario, descricao, custo):
    session = Session()
    manutencao = Manutencao(
        ID_funcionario=id_funcionario,
        descricao=descricao,
        custo=custo
    )
    session.add(manutencao)
    session.commit()
    session.close()

def listar_manutencoes():
    session = Session()
    manutencoes = session.query(Manutencao).all()
    session.close()
    return manutencoes

# Funções para Rota
def add_rota(tempo_estimado):
    session = Session()
    rota = Rota(
        Tempo_estimado=tempo_estimado
    )
    session.add(rota)
    session.commit()
    session.close()

def listar_rotas():
    session = Session()
    rotas = session.query(Rota).all()
    session.close()
    return rotas