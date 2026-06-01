'''
controlador.py
O Cérebro. Valida se os campos
estão vazios, converte textos para
números e faz a ponte segura entre
a Interface e o Modelo.
'''
from modelo import Modelo


class Controlador:

    def __init__(self):
        self.modelo = Modelo()

    def salvar_produto(self, nome, preco, quantidade):

        try:
            preco = float(preco)
            quantidade = int(quantidade)

            self.modelo.salvar_produto(
                nome,
                preco,
                quantidade
            )

            return True

        except ValueError:
            return False

    def buscar_produto(self):
        return self.modelo.buscar_produto()