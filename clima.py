import requests  
import telebot
import emoji

API_TOKEN = '7149422129:AAGsW-xgkI0aOt8kpCvy_TkoCXMxBYR6krM'

bot = telebot.TeleBot(API_TOKEN)

API_KEY = '1657642b5f12fdfa6560d69231aed5a1'  

@bot.message_handler(commands=['clima', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Digite o nome da cidade para ver o clima')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    cidade = message.text
    # Monta a URL da API com base na chave e na cidade inserida.
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br'
    
    requisicao = requests.get(link)  # Faz uma solicitação GET para a API OpenWeatherMap com a URL construída anteriormente.

    requisicao_dic = requisicao.json()  # Converte a resposta da solicitação em um dicionário Python.

    descricao = requisicao_dic['weather'][0]['description']
    temp_min = requisicao_dic['main']['temp_min'] - 273.15  # Converte Kelvin para Celsius
    temp_max = requisicao_dic['main']['temp_max'] - 273.15  # Converte Kelvin para Celsius

    if descricao == 'nublado' or descricao == 'algumas nuvens' or descricao == 'nuvens dispersas': 
        resposta = f'Dados climáticos atualizados de {cidade}:\n \n Clima: {descricao} {emoji.emojize(":cloud:")} \n Minima de {temp_min:.2f}\n Máxima de {temp_max:.2f} '
        print(requisicao_dic)
   
    elif descricao == 'chuva leve':
        resposta = f'Dados climáticos atualizados de {cidade}:\n Clima: {descricao} {emoji.emojize(":cloud_with_rain: ")} \n Minima de {temp_min:.2f}\n Máxima de {temp_max:.2f} '
   
    elif descricao == 'céu limpo':
        resposta = f'Dados climáticos atualizados de {cidade}:\n Clima: {descricao} {emoji.emojize(":sun:")}  \n Minima de {temp_min:.2f}\n Máxima de {temp_max:.2f} '
   
    elif descricao == 'névoa':
        resposta = f'Dados climáticos atualizados de {cidade}:\n Clima: {descricao} {emoji.emojize(":fog:")}  \n Minima de {temp_min:.2f}\n Máxima de {temp_max:.2f} '
  
    elif descricao == 'chuva moderada ':
       resposta = f'Dados climáticos atualizados de {cidade}:\n Clima: {descricao} {emoji.emojize("	:cloud_with_rain:")}  \n Minima de {temp_min:.2f}\n Máxima de {temp_max:.2f} '

    else:
         resposta = f'Dados climáticos atualizados de {cidade}:\n Clima: {descricao} \n Minima de {temp_min:.2f}\n Máxima de {temp_max:.2f} '
    bot.reply_to(message, resposta)

bot.infinity_polling()
