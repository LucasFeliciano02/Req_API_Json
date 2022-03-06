"""
Json - formato / dicionario do python
JavaScript Object Notation
é um formato de troca de dados entre sistemas e programas muito leve
e de fácil utilização. muito utilizado por APIs
"""

from dados import *
import json

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)
