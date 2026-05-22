'''
modelo.py (Model)
Comunica com o sqlite3. Tem as
funções de conectar, criar a tabela
produtos e comandos SQL diretos
(INSERT, SELECT, UPDATE,
DELETE).
'''
import sqlite3

def conectar():
    return sqlite3.connect("banco_dados.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        ''' CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco INTEGER NOT NULL,
        qtd INTEGER NOT NULL)
''')
    
    conexao.commit()
    conexao.close()


def inserir_produtos(nome_prod, preco, qtd):
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n--- Novo Produto ---\n")
    nome_prod = input("Nome do produto: ")
    preco = float(input("Preço unitário do produto(R$): "))
    qtd = int(input("Quantidade: "))

    cmd_sql = "INSERT INTO produtos (nome, preco, qtd) VALUES (?, ?, ?)"

    cursor.execute(cmd_sql, (nome_prod, preco, qtd))

    conexao.commit()
    print("Produto cadastrado com sucesso!")

def buscar_produto():
    print("\n--- Lista de Produtos ---\n")
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT id, nome FROM produtos")
    resulato = cursor.fetchall()
    if len(resulato) == 0:
        print("Nenhum produto cadastrado ainda.")
    else:
        print("\n--- Produtos ---\n")
        for linha in resulato:
            print(f"ID: {linha[0]} | Nome: {linha[1]}")
    
    conexao.close


def atualizar_preco():
    print("\n--- Atualizar Preço ---\n")
    conexao = conectar()
    cursor = conexao.cursor()

    id_prod = int(input("Qual o ID do produto a ser atualizado: "))
    novo_preco = float(input("Novo preço: "))

    cmd_sql = "UPDATE produtos SET preco = ? WHERE id = ?"

    cursor.execute(cmd_sql, (novo_preco, id_prod))
    conexao.commit()
    
    if cursor.rowcount == 0:
        print("❌ ERRO: Produto não localizado!")
    else:
        print("✅ Produto atualizado com sucesso!")

    conexao.close()


def deletar_produto(id_del):
    print("\n--- Deletar Produto ---\n")
    conexao = conectar()
    cursor = conexao.cursor()

    id_del = int(input("Qual o ID a ser deletado: "))
    sql_del = "DELET FROM produtos WHERE id = ?"

    cursor.execute(sql_del, (id_del, ))
    conexao.commit()

    if cursor.rowcount == 0:
        print("❌ Produto não existe.")
    else:
        print("✅ Produto deletado com sucesso!")

    conexao.commit()
    conexao.close()




