from models import session, Veiculo, Manutencao

def add_manutencao(descricao, data, veiculo_id, session):
    if descricao == "" or data == "" or veiculo_id == "":
        print("Descrição, data e veículo são obrigatórios")
        return
    veiculo = session.get(Veiculo, veiculo_id)
    if veiculo is None:
        print("Veículo não encontrado")
        return
    manutencao = Manutencao(descricao=descricao, data=data, veiculo_id=veiculo_id)
    session.add(manutencao)
    session.commit()
    print(f"Manutenção {descricao} cadastrada com sucesso!")

def delete_manutencao(id_manutencao, session):
    try:
        id_manutencao = int(id_manutencao)
    except ValueError:
        print("ID inválido")
        return
    manutencao = session.get(Manutencao, id_manutencao)
    if manutencao is None:
        print("Manutenção não encontrada")
        return
    session.delete(manutencao)
    session.commit()
    print(f"Manutenção {manutencao.descricao} excluída com sucesso")

def list_manutencoes(session):
    manutencoes = session.query(Manutencao).all()
    if manutencoes:
        for manutencao in manutencoes:
            veiculo = session.get(Veiculo, manutencao.veiculo_id)
            print(f"ID: {manutencao.id}, Descrição: {manutencao.descricao}, Data: {manutencao.data}, Veículo: {veiculo.modelo} - {veiculo.placa} - {veiculo.ano}")
    else:
        print("Nenhuma manutenção cadastrada")
