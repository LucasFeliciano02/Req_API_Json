'''

entrar no site pegar os dados e xibir, mandar por email,é muito util quando o site
nao te fornece um api para achar recursos no site

'''

import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(f'\n{data.text}', f'\n{titulo.text}', f'\n{votos.text}', sep='\n')
