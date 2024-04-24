import shutil
from tkinter import *
import sqlite3
import pandas as pd
from datetime import datetime


class Functions:

    def variaveis(self):
        self.cod = self.codigoEntry.get()
        self.nomeProduto = self.produtoEntry.get()
        self.categoria = self.categoriaEntry.get()
        self.distribuidora = self.distribuidoraEntry.get()
        self.quantidade = self.quantidadeEntry.get()

    def limparCampos(self):
        self.codigoEntry.delete(0, END)
        self.produtoEntry.delete(0, END)
        self.categoriaEntry.delete(0, END)
        self.distribuidoraEntry.delete(0, END)
        self.quantidadeEntry.delete(0, END)

    def conectarBancoDeDados(self):
        self.connection = sqlite3.connect("estoque.bd")
        self.cursor = self.connection.cursor()
        print("\033[32mConectou com o Banco de Dados!\033[m")

    def desconectarBancoDeDados(self):
        self.connection.close()
        print("\033[31mDesconectou com o Banco de Dados!\033[m")

    def criarTabelaProduto(self):
        self.conectarBancoDeDados()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
        cod INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeProduto CHAR(20) NOT NULL,
        categoria CHAR(15),
        distribuidora CHAR(50) NOT NULL,
        quantidadeProduto INTEGER NOT NULL
        );
        """)
        self.connection.commit()
        print("\033[32mTabela Produtos criada com sucesso!\033[m")
        self.desconectarBancoDeDados()

    def cadastrarProduto(self):
        self.conectarBancoDeDados()
        self.variaveis()
        self.cursor.execute("""
        INSERT INTO produtos (nomeProduto, categoria, distribuidora, quantidadeProduto) VALUES (?, ?, ?, ?)
        """, (self.nomeProduto, self.categoria, self.distribuidora, self.quantidade))
        self.connection.commit()
        self.desconectarBancoDeDados()
        self.exibirDadosTabelaProduto()
        self.limparCampos()

    def exibirDadosTabelaProduto(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conectarBancoDeDados()
        self.dados = self.cursor.execute("""
        SELECT cod, nomeProduto, categoria, distribuidora, quantidadeProduto FROM produtos
        """)
        for dado in self.dados:
            self.tabela.insert("", END, values=dado)
        self.desconectarBancoDeDados()

    def apagarProduto(self):
        item_selecionado = self.tabela.selection()
        cod_produto = self.tabela.item(item_selecionado)['values'][0]
        self.conectarBancoDeDados()
        self.cursor.execute("""
            DELETE FROM produtos 
            WHERE cod=?
            """, (cod_produto,))
        self.connection.commit()
        self.desconectarBancoDeDados()

        self.tabela.delete(item_selecionado)

    def inserirDadosEntries(self, cod, produto, categoria, distribuidora, quantidade):
        self.codigoEntry.insert(0, cod)
        self.produtoEntry.insert(0, produto)
        self.categoriaEntry.insert(0, categoria)
        self.distribuidoraEntry.insert(0, distribuidora)
        self.quantidadeEntry.insert(0, quantidade)

    def one_double_click(self, event):
        self.limparCampos()
        item_selecionado = self.tabela.selection()
        valores_selecionados = self.tabela.item(item_selecionado)['values']
        cod = valores_selecionados[0]
        produto = valores_selecionados[1]
        categoria = valores_selecionados[2]
        distribuidora = valores_selecionados[3]
        quantidade = valores_selecionados[4]
        self.inserirDadosEntries(cod, produto, categoria, distribuidora, quantidade)

    def alterarProduto(self):

        self.conectarBancoDeDados()
        self.variaveis()
        self.cursor.execute("""
            UPDATE produtos 
            SET nomeProduto=?, categoria=?, distribuidora=?, quantidadeProduto=? 
            WHERE cod=?
            """, (self.nomeProduto, self.categoria, self.distribuidora, self.quantidade, self.cod))

        self.connection.commit()
        self.desconectarBancoDeDados()
        self.exibirDadosTabelaProduto()
        self.limparCampos()

    def extrairDados(self):
        estoque = dict()
        cod = list()
        nomeProduto = list()
        categoria = list()
        distribuidora = list()
        quantidadeProduto = list()
        self.conectarBancoDeDados()
        self.dados = self.cursor.execute("""
        SELECT cod, nomeProduto, categoria, distribuidora, quantidadeProduto FROM produtos""")
        for dado in self.dados:
            cod.append(dado[0])
            nomeProduto.append(dado[1])
            categoria.append(dado[2])
            distribuidora.append(dado[3])
            quantidadeProduto.append(dado[4])
        self.desconectarBancoDeDados()
        estoque["Cod"] = cod
        estoque["Nome Do Produto"] = nomeProduto
        estoque["Categoria"] = categoria
        estoque["Distribuidora"] = distribuidora
        estoque["Quantidade De Produtos"] = quantidadeProduto
        dataFrameEstoque = pd.DataFrame(estoque)
        dataFrameEstoque.to_excel('Estoque.xlsx')

    def salvarDados(self):
        self.dataAtual()
        shutil.copy(src="estoque.bd", dst=f"backup/estoque_{self.data}.bd", follow_symlinks=False)

    def dataAtual(self):
        dia = datetime.now().day
        if datetime.now().month < 10:
            mes = f"0{datetime.now().month}"
        else:
            mes = datetime.now().month
        ano = datetime.now().year
        self.data = f"{dia}-{mes}-{ano}"

    def buscarProduto(self):
        self.variaveis()
        self.conectarBancoDeDados()
        dados = self.cursor.execute("""
        SELECT cod, nomeProduto, categoria, distribuidora, quantidadeProduto FROM produtos where cod=?""", (self.cod))
        self.limparCampos()
        for dado in dados:
            cod = dado[0]
            produto = dado[1]
            categoria = dado[2]
            distribuidora = dado[3]
            quantidade = dado[4]
            self.inserirDadosEntries(cod, produto, categoria, distribuidora, quantidade)
        self.desconectarBancoDeDados()

# teste = Functions()
# teste.buscarProduto()
