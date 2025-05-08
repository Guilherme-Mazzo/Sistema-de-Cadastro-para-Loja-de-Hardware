# Lista que vai armazenar o cadastro das empresas (Clientes)
# Formato de dicionário dentro de uma lista para adicionar as chaves e valores
lista_empresas = [
    {
        "nome_empresa": " ",
        "id_empresa": " "
    }
]

# Função para adicionar uma nova empresa à lista
def registrar_empresa(nome_empresa, id_empresa):
    nova_empresa = {
        "nome_empresa": nome_empresa,
        "id_empresa": id_empresa
    }
    lista_empresas.append(nova_empresa)

# Menu para cadastro de empresas
def menu_empresas():
    while True:
        print("\n=== MÓDULO DE EMPRESAS ===")
        nome_empresa = input("Digite o nome da empresa: ")
        id_empresa = input("Digite o número do ID: ")

        registrar_empresa(nome_empresa, id_empresa)

        continuar = input("Deseja adicionar outra empresa? (s/n): ").lower()
        if continuar != 's':
            break

    print("\nLista de empresas cadastradas:")
    for empresa in lista_empresas:
        print(empresa)

# Apenas executa testes se o arquivo for rodado diretamente
if __name__ == "__main__":
    menu_empresas()
