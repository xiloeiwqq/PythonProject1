import os

import requests
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount, from_currency):
    """функция для конвертации суммы из одной валюты в рубли"""
    if from_currency not in ['USD', 'EUR']:
        raise ValueError("поддерживаются только валюты USD и EUR")

    url = f"https://api.apilayer.com/exchangerates_data/convert"

    params = {
        "from": from_currency,
        "to": "RUB",
        "amount": amount
    }

    headers = {
        "apikey": API_KEY
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['result']
    else:
       raise Exception(f"ошибка при обращении к API: {response.status_code}")


def process_transaction(transaction):
    """функция для обработки транзакции и получения суммы в рублях"""
    amount = transaction['amount']
    currency = transaction['currency']

    if currency in ['USD', 'EUR']:
        return convert_to_rub(amount, currency)

    elif currency == 'RUB':
        return amount

    raise ValueError(f"валюта {currency} не поддерживается")