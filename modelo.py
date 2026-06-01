'''
modelo.py (Model)
Comunica com o sqlite3. Tem as
funções de conectar, criar a tabela
produtos e comandos SQL diretos
(INSERT, SELECT, UPDATE,
DELETE).
'''
import sqlite3


class Modelo:
    def __init__(self):
        self.conexao = sqlite3.connect("banco.db")
        self.cursor = self.conexao.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
        """)

        self.conexao.commit()

    def salvar_produto(self, nome, preco, quantidade):
        self.cursor.execute("""
        INSERT INTO produtos(nome, preco, quantidade)
        VALUES (?, ?, ?)
        """, (nome, preco, quantidade))

        self.conexao.commit()

    def buscar_produto(self):
        self.cursor.execute("""
        SELECT nome, quantidade
        FROM produtos
        """)

        return self.cursor.fetchall()



