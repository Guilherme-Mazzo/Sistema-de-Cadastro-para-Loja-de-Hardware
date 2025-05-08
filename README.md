
# 🛠️ Sistema de Cadastro para Loja de Hardware

Este é um sistema simples de cadastro de produtos, vendas, compras e clientes, feito em Python com interface via terminal. Ideal para fins educacionais e para praticar modularização de código.

---

## 📌 Funcionalidades

- Cadastro de **produtos de hardware**
- Registro de **vendas**
- Registro de **compras para estoque**
- Cadastro de **empresas/clientes**
- Menu interativo para navegação no terminal

---

## 📁 Estrutura de Arquivos

├── app.py # Arquivo principal com o menu do sistema
├── compra.py # Cadastro de compras
├── empresas.py # Cadastro de empresas
├── hardware.py # Cadastro de produtos
├── vendas.py # Cadastro de vendas


---

## ▶️ Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone o repositório ou copie os arquivos.
3. Execute o arquivo principal:

```bash
python app.py
Escolha uma opção no menu e siga as instruções para cadastrar os dados.

📂 Descrição dos Módulos
app.py
Exibe o menu principal.

Redireciona para o módulo de acordo com a opção escolhida.

hardware.py
Permite cadastrar produtos com:

ID do produto

Nome

Preço original

Preço promocional

vendas.py
Permite registrar vendas com:

ID da venda

ID do hardware

ID da empresa

Data da venda

Valor

compra.py
Permite registrar compras de estoque com:

ID da compra

Data da compra

Valor

Nome do produto

empresas.py
Permite cadastrar empresas com:

Nome

ID

💡 Possíveis Melhorias Futuras
 Persistência de dados em arquivos (.json ou .csv)

 Conexão com banco de dados (SQLite, MySQL)

 Interface gráfica com Tkinter ou PyQt

 Sistema de autenticação de usuários

 Criação de relatórios de vendas e estoque

✅ Requisitos
Python 3.7 ou superior

Terminal para executar o programa

🧠 Aprendizados Envolvidos
Modularização em Python

Estruturas de dados (listas e dicionários)

Entrada e saída no terminal

Organização de projetos

📜 Licença
Este projeto é livre para uso educacional. Sinta-se à vontade para modificar e reutilizar.
