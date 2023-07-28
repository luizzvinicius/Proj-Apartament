# Projeto apartamento
Projeto feito com Python e PostgreSQL que simula a portaria de um prédio.

## Acompanhe o modelo relacional:
<div align="center">
  <img src="https://github.com/luizzvinicius/Atividades-Python/assets/93850693/2ee9fffb-7fb5-4119-9366-29f4fa79e682">
</div>

## Configurações:
### 1. Instale o módulo que lida com arquivos .env em Python.
`pip install dot-env`

Configure um arquivo .env com as seguintes variáveis:
* last_bloco = blocos que contém no seu condomínio<br>
* db_name = nome do banco<br>
* host = URL do banco de dados<br>
* user = seu usuário Postgre<br>
* password = sua senha Postgre<br>
* port = porta do banco de dados

### 2. Instale o módulo que faz a conexão com o PostgreSQL.
`pip install psycopg2` <br><br>
É necessário criar o banco de dados no PgAdmin antes de executar o projeto.<br>
As tabelas estão no arquivo `data_base.sql`

Feito isso, é só executar o arquivo main.py

### 3. Caso deseje, instale a biblioteca de testes pytest
Há alguns arquivos de teste para a validação das funções de formatação, etc.
