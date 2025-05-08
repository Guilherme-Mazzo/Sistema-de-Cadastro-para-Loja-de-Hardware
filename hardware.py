# Lista que vai armazenar os produtos de hardware
lista_hard = [
    {
        "id_produto": " ",
        "nome_hard": " ",
        "original_price": " ",
        "promotion_price": " "
    }
]

# Função para adicionar um novo produto à lista de hardware
def registrar_hardware(id_produto, nome_hard, original_price, promotion_price):
    novo_produto = {
        "id_produto": id_produto,
        "nome_hard": nome_hard,
        "original_price": original_price,
        "promotion_price": promotion_price
    }
    lista_hard.append(novo_produto)

# Menu para cadastro de hardware
def menu_hardware():
    while True:
        print("\n=== MÓDULO DE HARDWARE ===")
        id_produto = input("Digite o número do ID: ")
        nome_hard = input("Digite o nome do produto: ")
        original_price = input("Digite o valor original do produto: ")
        promotion_price = input("Digite o valor promocional do produto: ")

        registrar_hardware(id_produto, nome_hard, original_price, promotion_price)

        continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nLista de produtos cadastrados:")
    for produto in lista_hard:
        print(produto)

# Apenas executa testes se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu_hardware()
