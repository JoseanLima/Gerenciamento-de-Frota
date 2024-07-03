from crud_operations import add_motorista, get_motorista, update_motorista, delete_motorista, list_motoristas
from crud_operations import agendar_manutencao, listar_manutencoes
from crud_operations import add_rota, listar_rotas

def main_menu():
    while True:
        print("Escolha opão:")
        print("(1) Cadastrar Motorista")
        print("(2) Alterar Motorista")
        print("(3) Excluir Motorista")
        print("(4) Localizar Motorista")
        print("(5). Listar Motoristas")
        print("(6) Agendar Manutenção")
        print("(7) Listar Manutenções")
        print("(8) Cadastrar Rota")
        print("(9) Listar Rotas")
        print("(0) Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            quilometragem = float(input("Quilometragem: "))
            quilometragemRodada = float(input("Quilometragem Rodada: "))
            consumo = float(input("Consumo: "))
            marca = input("Marca: ")
            placa = input("Placa: ")
            add_motorista(nome, cpf, quilometragem,
                          quilometragemRodada, consumo, marca, placa)
            print("Motorista cadastrado com sucesso!")
        elif escolha == '2':
            id_funcionario = int(input("ID do Motorista: "))
            nome = input("Novo Nome: ")
            update_motorista(id_funcionario, nome=nome)
            print("Motorista atualizado com sucesso!")
        elif escolha == '3':
            id_funcionario = int(input("ID do Motorista: "))
            delete_motorista(id_funcionario)
            print("Motorista excluído com sucesso!")
        elif escolha == '4':
            id_funcionario = int(input("ID do Motorista: "))
            motorista = get_motorista(id_funcionario)
            print(motorista)
        elif escolha == '5':
            motoristas = list_motoristas()
            for motorista in motoristas:
                print(motorista)
        elif escolha == '6':
            id_funcionario = int(input("ID do Motorista: "))
            descricao = input("Descrição da Manutenção: ")
            custo = float(input("Custo da Manutenção: "))
            agendar_manutencao(id_funcionario, descricao, custo)
            print("Manutenção agendada com sucesso!")
        elif escolha == '7':
            manutencoes = listar_manutencoes()
            for manutencao in manutencoes:
                print(manutencao)
        elif escolha == '8':
            tempo_estimado = int(input("Tempo estimado: "))
            add_rota(tempo_estimado)
            print("Rota cadastrada com sucesso!")
        elif escolha == '9':
            rotas = listar_rotas()
            for rota in rotas:
                print(rota)
        elif escolha == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main_menu()
