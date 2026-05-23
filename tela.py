'''
tela.py (View)
A Interface. Desenha botões, caixas
(CTkEntry), lida com pop-ups de
erro e o gráfico do Matplotlib.
'''
import customtkinter as ctk
from customtkinter import CTkMessagebox
from modelo import inserir_produtos, buscar_produto, atualizar_preco, deletar_produto
from controlador import processar_cadastro





while True:
    print("\n===============================\n")    
    print("Sistema de Gestão de Inventário")
    print("\n===============================\n")
    print("[1] Inserir Produto")
    print("[2] Buscar Produto")
    print("[3] Atualizar Preço")
    print("[4] Deletar Produto")
    print("[0] Sair")

    opcao = input("Escolha um opção: ")

    match opcao:
        case "1":
            inserir_produtos()
        case "2":
            buscar_produto()
        case "3":
            atualizar_preco()
        case "4":
            deletar_produto()
        case"0":
            print("Desligando o sistema... até mais!")
            break
        case _:
            print("❌ Opção inválida. Tente novamente.")
            
