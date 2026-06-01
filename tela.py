'''
tela.py (View)
A Interface. Desenha botões, caixas
(CTkEntry), lida com pop-ups de
erro e o gráfico do Matplotlib.
'''
import customtkinter as ctk

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from controlador import Controlador


class Tela:

    def __init__(self):

        self.controlador = Controlador()

        self.janela = ctk.CTk()
        self.janela.geometry("900x600")
        self.janela.title("Sistema de Gestão")

        titulo = ctk.CTkLabel(
            self.janela,
            text="Cadastro de Produtos",
            font=("Arial", 24)
        )

        titulo.pack(pady=10)

        self.entry_nome = ctk.CTkEntry(
            self.janela,
            placeholder_text="Nome"
        )

        self.entry_nome.pack(pady=5)

        self.entry_preco = ctk.CTkEntry(
            self.janela,
            placeholder_text="Preço"
        )

        self.entry_preco.pack(pady=5)

        self.entry_qtd = ctk.CTkEntry(
            self.janela,
            placeholder_text="Qtd"
        )

        self.entry_qtd.pack(pady=5)

        botao_salvar = ctk.CTkButton(
            self.janela,
            text="Gravar Produto",
            command=self.salvar
        )

        botao_salvar.pack(pady=10)

        botao_grafico = ctk.CTkButton(
            self.janela,
            text="Gerar Gráfico",
            command=self.gerar_grafico
        )

        botao_grafico.pack(pady=10)

        self.frame_grafico = ctk.CTkFrame(
            self.janela,
            width=600,
            height=300
        )

        self.frame_grafico.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.janela.mainloop()

    def salvar(self):

        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        qtd = self.entry_qtd.get()

        resultado = self.controlador.salvar_produto(
            nome,
            preco,
            qtd
        )

        if resultado:

            # UX
            self.entry_nome.delete(0, "end")
            self.entry_preco.delete(0, "end")
            self.entry_qtd.delete(0, "end")

    def gerar_grafico(self):

        dados = self.controlador.buscar_produto()

        nomes = []
        quantidades = []

        for produto in dados:
            nomes.append(produto[0])
            quantidades.append(produto[1])

        figura = plt.Figure(
            figsize=(6, 4),
            dpi=100
        )

        grafico = figura.add_subplot(111)

        grafico.bar(
            nomes,
            quantidades
        )

        grafico.set_title("Quantidade por Produto")

        canvas = FigureCanvasTkAgg(
            figura,
            master=self.frame_grafico
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill="both",
            expand=True
        )


Tela()