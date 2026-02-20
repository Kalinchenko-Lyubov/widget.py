import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
HEADERS = {"apikey": API_KEY}


def get_sum_transaction_rub(transaction: Dict[str, dict]) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    if not transaction:
        print("Транзакция не предоставлена!")
        return None

    try:
        amount_str = transaction["operationAmount"]["amount"]
        currency_code = transaction["operationAmount"]["currency"]["code"]
    except KeyError as exc:
        raise ValueError(f"Транзакция неполная: {exc}")

    if currency_code == "RUB":
        return float(amount_str)

    params = {"to": "RUB", "from": currency_code, "amount": amount_str}

    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        converted_amount = response.json()["result"]
        return float(converted_amount)
    else:
        raise Exception(f"Ошибка конвертации валюты: {response.text}")
