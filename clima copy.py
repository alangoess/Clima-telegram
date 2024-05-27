import requests  
import telebot

API_TOKEN = '7149422129:AAGsW-xgkI0aOt8kpCvy_TkoCXMxBYR6krM'

bot = telebot.TeleBot(API_TOKEN)

API_KEY = '1657642b5f12fdfa6560d69231aed5a1'  
cidade = input('digite: ')

link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'
    
requisicao = requests.get(link)  # Faz uma solicitação GET para a API OpenWeatherMap com a URL construída anteriormente.

requisicao_dic = requisicao.json()  # Converte a resposta da solicitação em um dicionário Python.

descricao = requisicao_dic['weather'][0]['description']
temp_min = requisicao_dic['main']['temp_min'] - 273.15  # Converte Kelvin para Celsius
temp_max = requisicao_dic['main']['temp_max'] - 273.15  # Converte Kelvin para Celsius
print(requisicao_dic)
    
  
