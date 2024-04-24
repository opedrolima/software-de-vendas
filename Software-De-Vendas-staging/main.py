from functions import *
from customtkinter import CTkEntry, CTkButton
from tkinter import ttk

window = Tk()


class Application(Functions):
    def __init__(self):
        self.window = window
        self.telaGeral()
        self.framesDaTela()
        self.widgetsFrame1()
        self.tabelaProduto()
        self.criarTabelaProduto()
        self.exibirDadosTabelaProduto()
        self.window.mainloop()

    def telaGeral(self):
        self.window.title("Software De Vendas")
        self.window.config(background="white")
        self.window.geometry("720x600")
        self.window.minsize(width=590, height=500)

    def framesDaTela(self):
        self.frame1 = Frame(self.window, background="#DDD51E")
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=0.4)

        self.frame2 = Frame(self.window)
        self.frame2.place(relx=0, rely=0.4, relwidth=1, relheight=0.6156)

    def widgetsFrame1(self):
        # Labels and Entries
        self.lbCodigo = Label(self.frame1,
                              text="Código",
                              background="#DDD51E",
                              foreground="black",
                              font="MartelSans 12 bold")
        self.lbCodigo.place(relx=0.015, rely=0.03)
        self.codigoEntry = CTkEntry(self.frame1,
                                    corner_radius=50,
                                    border_color="white",
                                    fg_color="white",
                                    text_color="black",
                                    border_width=0)
        self.codigoEntry.place(relx=0.015, rely=0.13, relwidth=0.11, relheight=0.11)

        self.lbProduto = Label(self.frame1,
                               text="Produto",
                               background="#DDD51E",
                               foreground="black",
                               font="MartelSans 12 bold")
        self.lbProduto.place(relx=0.015, rely=0.30)
        self.produtoEntry = CTkEntry(self.frame1,
                                     corner_radius=50,
                                     border_color="white",
                                     fg_color="white",
                                     text_color="black",
                                     border_width=0)
        self.produtoEntry.place(relx=0.015, rely=0.40, relwidth=0.32, relheight=0.11)

        self.lbCategoria = Label(self.frame1,
                                 text="Categoria",
                                 background="#DDD51E",
                                 foreground="black",
                                 font="MartelSans 12 bold")
        self.lbCategoria.place(relx=0.42, rely=0.30)
        self.categoriaEntry = CTkEntry(self.frame1,
                                       corner_radius=50,
                                       border_color="white",
                                       fg_color="white",
                                       text_color="black",
                                       border_width=0)
        self.categoriaEntry.place(relx=0.42, rely=0.40, relwidth=0.15, relheight=0.11)

        self.lbDistribuidora = Label(self.frame1,
                                     text="Distribuidora",
                                     background="#DDD51E",
                                     foreground="black",
                                     font="MartelSans 12 bold")
        self.lbDistribuidora.place(relx=0.015, rely=0.60)
        self.distribuidoraEntry = CTkEntry(self.frame1,
                                           corner_radius=50,
                                           border_color="white",
                                           fg_color="white",
                                           text_color="black",
                                           border_width=0)
        self.distribuidoraEntry.place(relx=0.015, rely=0.70, relwidth=0.32, relheight=0.11)

        self.lbQuantidade = Label(self.frame1,
                                  text="Quantidade",
                                  background="#DDD51E",
                                  foreground="black",
                                  font="MartelSans 12 bold")
        self.lbQuantidade.place(relx=0.42, rely=0.60)
        self.quantidadeEntry = CTkEntry(self.frame1,
                                        corner_radius=50,
                                        border_color="white",
                                        fg_color="white",
                                        text_color="black",
                                        border_width=0)
        self.quantidadeEntry.place(relx=0.42, rely=0.70, relwidth=0.15, relheight=0.11)

        # Buttons
        self.limparButton = CTkButton(self.frame1,
                                      corner_radius=50,
                                      text="Limpar",
                                      fg_color="white",
                                      text_color="black",
                                      border_width=0,
                                      hover_color="light gray",
                                      font=("MartelSans", 15, "bold"),
                                      command=self.limparCampos)

        self.limparButton.place(relx=0.15, rely=0.12, relwidth=0.13, relheight=0.12)

        self.buscarButton = CTkButton(self.frame1,
                                      corner_radius=50,
                                      text="Buscar",
                                      fg_color="white",
                                      text_color="black",
                                      border_width=0,
                                      hover_color="light gray",
                                      font=("MartelSans", 15, "bold"),
                                      command=self.buscarProduto)
        self.buscarButton.place(relx=0.3, rely=0.12, relwidth=0.13, relheight=0.12)

        self.novoButton = CTkButton(self.frame1,
                                    corner_radius=50,
                                    text="Novo",
                                    fg_color="white",
                                    text_color="black",
                                    border_width=0,
                                    hover_color="light gray",
                                    font=("MartelSans", 15, "bold"),
                                    command=self.cadastrarProduto)
        self.novoButton.place(relx=0.015, rely=0.87, relwidth=0.13, relheight=0.113)

        self.alterarButton = CTkButton(self.frame1,
                                       corner_radius=50,
                                       text="Alterar",
                                       fg_color="white",
                                       text_color="black",
                                       border_width=0,
                                       hover_color="light gray",
                                       font=("MartelSans", 15, "bold"),
                                       command=self.alterarProduto)
        self.alterarButton.place(relx=0.17, rely=0.87, relwidth=0.13, relheight=0.113)

        self.extrairButton = CTkButton(self.frame1,
                                       corner_radius=50,
                                       text="Extrair",
                                       fg_color="white",
                                       text_color="black",
                                       border_width=0,
                                       hover_color="light gray",
                                       font=("MartelSans", 15, "bold"),
                                       command=self.extrairDados)
        self.extrairButton.place(relx=0.325, rely=0.87, relwidth=0.13, relheight=0.113)

        self.salvarButton = CTkButton(self.frame1,
                                      corner_radius=50,
                                      text="Salvar",
                                      fg_color="white",
                                      text_color="black",
                                      border_width=0,
                                      hover_color="light gray",
                                      font=("MartelSans", 15, "bold"),
                                      command=self.salvarDados)
        self.salvarButton.place(relx=0.48, rely=0.87, relwidth=0.13, relheight=0.113)

        self.apagarButton = CTkButton(self.frame1,
                                      corner_radius=50,
                                      text="Apagar",
                                      fg_color="white",
                                      text_color="black",
                                      border_width=0,
                                      hover_color="light gray",
                                      font=("MartelSans", 15, "bold"),
                                      command=self.apagarProduto)
        self.apagarButton.place(relx=0.635, rely=0.87, relwidth=0.13, relheight=0.113)

    def tabelaProduto(self):
        self.style = ttk.Style(self.frame2)
        self.style.theme_use('clam')
        self.tabela = ttk.Treeview(self.frame2, height=3,
                                   columns=("column1", "column2", "column3", "column4", "column5"))
        self.tabela.heading("#0", text="")
        self.tabela.heading("#1", text="Cod")
        self.tabela.heading("#2", text="Produto")
        self.tabela.heading("#3", text="Categoria")
        self.tabela.heading("#4", text="Distribuidora")
        self.tabela.heading("#5", text="Quantidade")
        self.style.configure("Treeview.Heading", font=("MartelSans", 10, "bold"), borderwidth=1)
        self.tabela.column("#0", width=1, minwidth=0, stretch=NO, anchor="center")
        self.tabela.column("#1", width=20, minwidth=50, anchor="center")
        self.tabela.column("#2", width=160, minwidth=150, anchor="center")
        self.tabela.column("#3", width=105, minwidth=100, anchor="center")
        self.tabela.column("#4", width=160, minwidth=150, anchor="center")
        self.tabela.column("#5", width=50, minwidth=50, anchor="center")
        self.tabela.place(relx=0, rely=0, relwidth=0.97, relheight=1)
        self.scrollTabela = Scrollbar(self.frame2, orient="vertical", command=self.tabela.yview_scroll)
        self.tabela.config(yscrollcommand=self.scrollTabela.set)
        self.scrollTabela.place(relx=0.97, rely=0, relwidth=0.03, relheight=1)
        self.tabela.bind("<Double-1>", self.one_double_click)


Application()
