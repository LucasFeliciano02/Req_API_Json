"""
- API = APLICATION PROGRAMING INTERFACE  - programa criado para vc conseguir acessar algum sistema e trocar informacoes,
acessar um http e pegar informações que vem com essas apis

- Uma API Intermediaria feita pela empresa(google, instagram, facebook), ha regras que garantem que eu nao consiga ter acesso ao banco de dados direto,
só consigo ter acesso as informações que a api dele faz pra mim

- API nada mais é que um programa, microsite que a empresa(instagram por ex) cria pra pegar informações do banco de dados e passar
essas informações pra quem estiver pedindo pra ele, e essa api seta qual informações podem pedir, quem pode pedir, (gerencia)
e ele garante que vc nao tenha acesso a todo o banco de dados do instagram mas sim so a informação que o instagram permite voce 
ter acesso

- JSON  =  Comunicação (formato da informação, txt, pdf), eu peço a informação pra api e a api me da essa info como resposta
  é um dicionario python onde dentro desse dicionario tem as informações que aquela api esta te dando como resposta 

-------------------------------------------------------------------------------------------------------------------------------------------------------------

como acessar? ; ir em um site que exista uma api que procura

- request  =  VC pede uma informação para tal link que contem as informações
Dentro de uma pi há disponibilizado varios links onde cada link da um tipo de informação diferente

site: awesomeapi

api publica = da links de requisição em que vc consome informações dela

AO IMPORTAR, AS INFORMAÇÕES VEM EM FORMATO DE DICIONARIO JSON 

JSON - SE USA PARA TROCAR INFORMAÇÕES ENTRE SITES
APIS - NORMALMENTE VAO ENVIAR E PEGAR INFORMAÇÕES POR MEIO DESSE FORMATO QUE PRECISA MUDAR PARA UM FORMATO PYTHON
"""

import requests
import json
import time
import datetime

while True:
      cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
      cotacoes = cotacoes.json()  # AGORA COTACOES ESTÁ EM FORMATO PYTHON E NAO JSON MAIS

      cotacao_dolar = cotacoes['USDBRL']['bid']
      cotacao_euro = cotacoes['EURBRL']['bid']
      cotacao_bitcoin = cotacoes['BTCBRL']['bid']

      print('\n • COTAÇÕES EM TEMPO REAL:\n'), datetime.datetime.now()
      print(f' 1 Dólar: {cotacao_dolar} R$', f'\n 1 Euro: {cotacao_euro} R$',
            f'\n 1 Bitcoin: {cotacao_bitcoin} R$\n')
      
      time.sleep(5)
      
      # PARAMETRO 'Bid' É O QUE VE OS PRECOS NO CASO, POIS APARECE NO ARQUIVO.JSON DO SITE QUE POSSUI A API
      # print(cotacoes)  # ^TEM QUE TIRAR DO FORMATO JSON E COLOCAR NO FORMATO DO PYTHON PADRAO^
