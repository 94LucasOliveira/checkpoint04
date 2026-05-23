'''
modelo.py (Model)
Comunica com o sqlite3. Tem as
funções de conectar, criar a tabela
produtos e comandos SQL diretos
(INSERT, SELECT, UPDATE,
DELETE).
'''
import customtkinter as ctk
from customtkinter import CTkMessagebox
import random
import sqlite3
from tela import salvar_dados

def conectar():
    return sqlite3.connect("banco_dados.db")

def criar_tabela():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
    
        cursor.execute(
            ''' CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            qtd INTEGER NOT NULL)
    ''')
        
        conexao.commit()
        return conexao
    except sqlite3.Erro as e:
        print(f"Erro ao conectar ou criar tabela: {e}")
        raise

class AppCadastrarProduto(ctk.CTk):
    def __init__(janela):
        super().__init__()
        janela.geometry("400x400")
        janela.title("Cadastro de Produtos")

        lbl_produto = ctk.CTkLabel(janela, text="Novo Produto")
        lbl_produto.pack(pady=20)

        nome_prod = ctk.CTkEntry(janela, placeholder_text="Nome")
        nome_prod.pack(pady=10)

        preco = ctk.CTkEntry(janela, placeholder_text="Preço")
        preco.pack(pady=10)

        qtd = ctk.CTkEntry(janela, placeholder_text="Qunatidade")
        qtd.pack(pady=10)

        btn_salvar = ctk.CTkButton(janela, text="Salvar", command=inserir_produtos)
        btn_salvar.pack(pady=20) 

        ldl_mensagem = ctk.CTkLabel(janela, text="")
        ldl_mensagem.pack()

        janela.mainloop()        

def inserir_produtos(janela):
    janela.lbl_mensagem.configure()
    if not nome_prod or not preco or not qtd:
        raise ValueError("Todos os campos devem ser preenchidos.")
    
    
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n--- Novo Produto ---\n")
    nome_prod = (input("Nome do produto: "))
    try:    
        preco = float(input("Preço unitário do produto(R$): "))
        qtd = int(input("Quantidade: "))
    except ValueError:
        raise ValueError("Preço e qunatidade devem ser números válidos.")

    if preco <=0 or qtd <= 0:
        raise ValueError("Preço e quantidade devem ser maiores que zero.")

    if random.random() < 0.1: # 10% de chance de falha
        raise RuntimeError("Erro inesperado ao salvar no banco de dados.")
    
    print(f"Produto Salvo: Nome = {nome_prod}, Preço = {preco}, Quantidade = {qtd}")
    return True

    cmd_sql = "INSERT INTO produtos (nome, preco, qtd) VALUES (?, ?, ?)"

    cursor.execute(cmd_sql, (nome_prod, preco, qtd))

    conexao.commit()

    lbl_mensagem.configure(text="Produto inserido com sucesso!", text_color="green")

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




