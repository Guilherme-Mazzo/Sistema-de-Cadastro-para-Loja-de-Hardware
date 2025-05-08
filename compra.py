# Lista que armazena as compras
# Lista criada vazia, pois ela vai armazenar os inputs dos usuarios
lista_compra = [
    {
        "id_compra": " ",
        "date_buy": " ",
        "value": " ",
        "nm_produto_compra": " "
    }
]

# Função que adiciona uma nova compra à lista
def registrar_compra(id_compra, date_buy, value, nm_produto_compra):
    nova_compra = {
        "id_compra": id_compra,
        "date_buy": date_buy,
        "value": value,
        "nm_produto_compra": nm_produto_compra
    }
    lista_compra.append(nova_compra)  # Aqui ele vai armazenar os itens que vão entar dos inputs na lista_compra

# Menu do módulo de compras
def menu_compra():      # Criando a função onde vai ter o menu com a entrada dos dados
    while True:
        print("\n=== MÓDULO DE COMPRAS ===")
        id_compra = input("Digite o número do ID da compra: ")
        date_buy = input("Digite a data da compra (dd/mm/aaaa): ")
        value = input("Digite o valor da compra: ")
        nm_produto_compra = input("Digite o nome do produto comprado: ")

        registrar_compra(id_compra, date_buy, value, nm_produto_compra)  # Após receber os dados, vai acionar a função registrar compra para armazenar os dados dos inputs

        continuar = input("Deseja adicionar outra compra? (s/n): ").lower()    # Opção criada para verificar se o usuario desejar fazer um novo registro ou não
        if continuar != 's':  # Condição para verificar se deve continuar ou não os registros
            break

    print("\nLista de compras cadastradas:")
    for compra in lista_compra:     # Loop para pegar cada item  armazenado e exibir eles na tela
        print(compra)

# Apenas executa testes se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu_compra()
