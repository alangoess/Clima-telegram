import requests  # Importa o módulo 'requests', que permite fazer solicitações HTTP em Python.

API_KEY = '1657642b5f12fdfa6560d69231aed5a1'  # Define a chave da API OpenWeatherMap.

cidade = input('digite o nome da cidade para ver o clima: ')  # Solicita ao usuário que insira o nome da cidade.

# Monta a URL da API com base na chave e na cidade inserida.
link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'

requisicao = requests.get(link)  # Faz uma solicitação GET para a API OpenWeatherMap com a URL construída anteriormente.

requisicao_dic = requisicao.json()  # Converte a resposta da solicitação em um dicionário Python.
