import requests
import json


while True:
    try:
        cidade = input('Escreva sua cidade: ')

        tempo = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=7f6dbc6b05da5a8cebc4d01136d49526&lang=pt_br')
        tempo = json.loads(tempo.text)

        print('Condição do tempo:', tempo['weather'][0]['description'])
        print('Temperatura: ', float(tempo['main']['temp']) - 273.15)
    except:
        print('Cidade nao existe')
