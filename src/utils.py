import json
import os
from typing import Any, Dict, List


def get_transaction_data(file_path: str) -> List[Dict[str, Any]] | bool:
    """Возвращает данные о финансовых транзакциях"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, encoding="utf-8") as file:
            transaction_data = json.load(file)

        if isinstance(transaction_data, list):
            return transaction_data
        else:
            return []

    except json.JSONDecodeError:
        print("Ошибка декодирования файла")
        return []

    return []
