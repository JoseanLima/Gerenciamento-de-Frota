from models import session, Veiculo, Manutencao, Rota

def add_veiculo(placa, modelo, ano, session):
    if placa == "" or modelo == "" or ano == "":
        print("Placa, modelo e ano são obrigatórios")
        return
    if len(placa) != 7:
        print("Placa inválida")
        return
    if len(ano) != 4:
        print("Ano inválido")
        return
    veiculo = Veiculo(placa=placa, modelo=modelo, ano=ano)
    session.add(veiculo)
    session.commit()
    print(f"Veículo {modelo} cadastrado com sucesso!")

def update_veiculo(id_veiculo, placa, modelo, ano, session):
    veiculo = session.get(Veiculo, id_veiculo)
    if veiculo is None:
        print("Veículo não encontrado")
        return
    if placa != "":
        if len(placa) != 7:
            print("Placa inválida")
            return
        veiculo.placa = placa
    if modelo != "":
        veiculo.modelo = modelo
    if ano != "":
        if len(ano) != 4:
            print("Ano inválido")
            return
        veiculo.ano = ano
    session.commit()
    print(f"Veículo {veiculo.modelo} alterado com sucesso")

def delete_veiculo(id_veiculo, session):
    try:
        id_veiculo = int(id_veiculo)
    except ValueError:
        print("ID inválido")
        return
    veiculo = session.get(Veiculo, id_veiculo)
    if veiculo is None:
        print("Veículo não encontrado")
        return
    if session.query(Manutencao).filter_by(veiculo_id=id_veiculo).count() > 0:
        print("Veículo possui manutenções cadastradas")
        return
    if session.query(Rota).filter_by(veiculo_id=id_veiculo).count() > 0:
        print("Veículo possui rotas cadastradas")
        return
    session.delete(veiculo)
    session.commit()
    print(f"Veículo {veiculo.modelo} excluído com sucesso")

def list_veiculos(session):
    veiculos = session.query(Veiculo).all()
    if veiculos:
        for veiculo in veiculos:
            print(f"ID: {veiculo.id}, Modelo: {veiculo.modelo}, Placa: {veiculo.placa}, Ano: {veiculo.ano}")
    else:
        print("Nenhum veículo cadastrado")
