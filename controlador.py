'''
controlador.py
O Cérebro. Valida se os campos
estão vazios, converte textos para
números e faz a ponte segura entre
a Interface e o Modelo.
'''
from modelo import inserir_produtos

def processar_cadastro (nome, p_txt, q_txt):
    if nome == "" or p_txt == "":
        return False, "Campos vazios!"
    
    try:
        preco = float(p_txt)
        qtd = int(q_txt)
    except ValueError:
        return False, "Erro nos números!"
    
    inserir_produtos(nome, preco, qtd)
    return True, "Produto cadastrado!"
