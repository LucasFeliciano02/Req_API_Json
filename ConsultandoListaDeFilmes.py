"""
API - Aplication Programing Interfaces = interface que se comunica com outros programas
vc passa parametros e essa API te retorna informações
Existem milhares de APIS na internet que podem ser requisitadas atravez de requisiçoes web

Json - formato / dicionario do python
JavaScript Object Notation
é um formato de troca de dados entre sistemas e programas muito leve
e de fácil utilização. muito utilizado por APIs

"""

import requests
import json

req = None
sair = False

while sair == False:
   try:
      dict = requests.get('http://www.omdbapi.com/?apikey=5d9cabe3&t=' + input('Digite o nome do Filme: '))
      dict = json.loads(dict.text)
      print('Titulo:', dict['Title'])
      print('Ano:', dict['Year'])
      print('Escritor(es):', dict['Writer'])
      print('Atores:', dict['Actors'])
      print('Nota:', dict['imdbRating'])
   except:
      print('Erro no request. Ou limite de request diario atingido.')
      exit()