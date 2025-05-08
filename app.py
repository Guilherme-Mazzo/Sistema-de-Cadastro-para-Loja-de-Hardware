# As importações dos mudulos criados separadamente para cada opção
import compra
import empresas
import hardware
import vendas


# Função que cria o menu interativo com as opções de escolha para o usuario
def mostrar_menu():
    print("\n======================= MENU PRINCIPAL ============================")
    print("_____________________________________________________________________")
    print("\n********** DIGITE O NÚMERO CORRESPONDENTE À FUNÇÃO ESCOLHIDA **********")
    print("[1] - Cadastrar produtos de hardware")
    print("[2] - Cadastrar venda")
    print("[3] - Cadastrar compra")
    print("[4] - Cadastrar empresas")
    print("[0] - Sair")


# APP
def main():     # A função main() é responsável por manter o programa em execução até que o usuário decida sair.
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            hardware.menu_hardware()  # Chama o menu de hardware
        elif opcao == "2":
            vendas.menu_vendas()  # Chama o menu de vendas
        elif opcao == "3":
            compra.menu_compra()  # Chama o menu de compras
        elif opcao == "4":
            empresas.menu_empresas()  # Chama o menu de empresas
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
