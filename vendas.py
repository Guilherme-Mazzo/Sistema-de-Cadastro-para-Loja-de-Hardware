# Lista que vai armazenar as vendas
lista_vendas = [
    {
        "id_vendas": " ",
        "id_hardware": " ",
        "id_empresa": " ",
        "date_seller": " ",
        "value": " "
    }
]

# Função para adicionar uma nova venda à lista
def registrar_venda(id_vendas, id_hardware, id_empresa, date_seller, value):
    nova_venda = {
        "id_vendas": id_vendas,
        "id_hardware": id_hardware,
        "id_empresa": id_empresa,
        "date_seller": date_seller,
        "value": value
    }
    lista_vendas.append(nova_venda)

# Menu para cadastro de vendas
def menu_vendas():
    while True:
        print("\n=== MÓDULO DE VENDAS ===")
        id_vendas = input("Digite o número do ID da venda: ")
        id_hardware = input("Digite o número do ID do hardware: ")
        id_empresa = input("Digite o número do ID da empresa: ")
        date_seller = input("Digite a data da venda: ")
        value = input("Digite o valor da venda: ")

        registrar_venda(id_vendas, id_hardware, id_empresa, date_seller, value)

        continuar = input("Deseja adicionar outra venda? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nLista de vendas cadastradas:")
    for venda in lista_vendas:
        print(venda)

# Apenas executa testes se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu_vendas()
