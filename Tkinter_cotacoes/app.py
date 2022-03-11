"""
    Passos para transformar seu código em uma interface gráfica

Passo 1 = importar o tkinter
Passo 2 = Jogar seu código para dentro de uma função
Passo 3 = Criar sua janela usando o tkinter

"""

import requests
from tkinter import *


# criar a janela e dps agregar informações
# todo o codigo tem que estar dentro de uma função para utilizar o tkinter

def pegar_cotacoes():
    requisicao = requests.get(
        "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto


# * CRIANDO A JANELA TKINTER


janela = Tk()  # COMEÇA COM
janela.title('Cotação Atual das Moedas')
# janela.geometry('300x200')
janela.iconbitmap('cotacao.ico')  # icon do app
janela.resizable(width=FALSE, height=FALSE)


texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text='Buscas cotações Dólar/Euro/BTC', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='') 
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()  # TERMINA COM  # deixa a janela exibida, nao a fecha
