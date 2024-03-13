import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Agora você pode acessar a variável de ambiente como de costume

def currency_fetch(from_currency, to_currency, amount):

    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {
        "from": from_currency,
        "to": to_currency,
        "q": "1.0"
    }

    headers = {
        "X-RapidAPI-Key": os.environ.get('CURRENCY_KEY'),
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json() * amount
