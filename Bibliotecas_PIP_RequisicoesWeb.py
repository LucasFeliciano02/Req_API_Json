# biblioteca resquests = requisição web = entrar em um site
# ex navegador fazendo resposta a pagina pesquisada
# .get/ = pega informações .delete/ .post = pegar e enviar informações
# status - 200 = OK
# status 404 e 500 = erro
# headers é um metodo de passar parametro que fica dentro do requests


import requests

cabecalho = {'user-agent': 'Windows 12',
             'referer': 'https://google.com'}  # = cabeçalho padrao http

meus_cookies = {'ultima-visita': '10-10-2020'}

dados = {'username': 'Lucas',
         'password': 'Lu123'}

texto = None
try:
    requisicao = requests.post('https://putsreq.com/UYStyURah90AsLpgKKjo',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as ex:
    print('Requisição deu erro: ', ex)

print(texto)
