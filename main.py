from models import session
from manutencao import add_manutencao, delete_manutencao, list_manutencoes
from rota import add_rota, delete_rota, list_rotas
from veiculo import add_veiculo, update_veiculo, delete_veiculo, list_veiculos

def main_menu():
    while True:
        print("\nMenu de Operações")
        print("1. Cadastrar Veículo")
        print("2. Atualizar Veículo")
        print("3. Excluir Veículo")
        print("4. Listar Veículos")
        print("5. Cadastrar Manutenção")
        print("6. Excluir Manutenção")
        print("7. Listar Manutenções")
        print("8. Cadastrar Rota")
        print("9. Excluir Rota")
        print("10. Listar Rotas")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case '1':
                placa = input("Placa: ")
                modelo = input("Modelo: ")
                ano = input("Ano: ")
                add_veiculo(placa, modelo, ano, session)
            case '2':
                try:
                    id_veiculo = int(input("ID do Veículo: "))
                except ValueError:
                    print("ID inválido")
                    continue
                placa = input("Placa: ")
                modelo = input("Modelo: ")
                ano = input("Ano: ")
                update_veiculo(id_veiculo, placa, modelo, ano, session)
            case '3':
                try:
                    id_veiculo = int(input("ID do Veículo: "))
                except ValueError:
                    print("ID inválido")
                    continue
                delete_veiculo(id_veiculo, session)
            case '4':
                list_veiculos(session)
            case '5':
                descricao = input("Descrição: ")
                data = input("Data: ")
                veiculo_id = input("ID do Veículo: ")
                add_manutencao(descricao, data, veiculo_id, session)
            case '6':
                try:
                    id_manutencao = int(input("ID da Manutenção: "))
                except ValueError:
                    print("ID inválido")
                    continue
                delete_manutencao(id_manutencao, session)
            case '7':
                list_manutencoes(session)
            case '8':
                descricao = input("Descrição: ")
                veiculo_id = input("ID do Veículo: ")
                add_rota(descricao, veiculo_id, session)
            case '9':
                try:
                    id_rota = int(input("ID da Rota: "))
                except ValueError:
                    print("ID inválido")
                    continue
                delete_rota(id_rota, session)
            case '10':
                list_rotas(session)
            case '0':
                print("Saindo...")
                break
            case _:
                print("Opção inválida")

if __name__ == '__main__':
    main_menu()
