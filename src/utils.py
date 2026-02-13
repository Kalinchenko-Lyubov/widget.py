# Реализуйте функцию, которая принимает на вход путь до JSON-файла
# и возвращает список словарей с данными о финансовых транзакциях.
# Если файл пустой, содержит не список или не найден,
# функция возвращает пустой список.

import json
import os
from typing import List, Dict, Any


def get_transaction_data(file_path: str) -> List[Dict[str, Any]] | bool:
    """Возвращает данные о финансовых транзакциях"""

    transactions = []

    if not os.path.exists(file_path):
        return transactions

    try:
        with open(file_path, encoding='utf-8') as file:
            raw_data = json.load(file)

        if isinstance(raw_data, list):
            return raw_data
        else:
            return []

    except (json.JSONDecodeError, ValueError):
        print('Ошибка декодирования файла')
        return False

    return transactions
