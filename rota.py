from models import session, Veiculo, Rota

def add_rota(descricao, veiculo_id, session):
    if descricao == "" or veiculo_id == "":
        print("Descrição e veículo são obrigatórios")
        return
    veiculo = session.get(Veiculo, veiculo_id)
    if veiculo is None:
        print("Veículo não encontrado")
        return
    rota = Rota(descricao=descricao, veiculo_id=veiculo_id)
    session.add(rota)
    session.commit()
    print(f"Rota {descricao} cadastrada com sucesso!")

def delete_rota(id_rota, session):
    try:
        id_rota = int(id_rota)
    except ValueError:
        print("ID inválido")
        return
    rota = session.get(Rota, id_rota)
    if rota is None:
        print("Rota não encontrada")
        return
    session.delete(rota)
    session.commit()
    print(f"Rota {rota.descricao} excluída com sucesso")

def list_rotas(session):
    rotas = session.query(Rota).all()
    if rotas:
        for rota in rotas:
            veiculo = session.get(Veiculo, rota.veiculo_id)
            print(f"ID: {rota.id}, Descrição: {rota.descricao}, Veículo: {veiculo.modelo} - {veiculo.placa} - {veiculo.ano}")
    else:
        print("Nenhuma rota cadastrada")
