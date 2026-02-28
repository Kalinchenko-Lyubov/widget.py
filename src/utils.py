import json
import logging
import os
from typing import Any, Dict, List

# os.chdir("..")
# if not os.path.exists("logs"):
#     os.makedirs("logs")

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils_logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_data(file_path: str) -> List[Dict[str, Any]] | bool:
    """Возвращает данные о финансовых транзакциях"""
    logger.info("Выполняем проверку наличия информации о финансовых транзакциях")

    if not os.path.exists(file_path):
        logger.error(f"Файл {file_path} не найден.")
        return []
    try:
        logger.info("Открываем файл с транзакциями")
        with open(file_path, encoding="utf-8") as file:
            transaction_data = json.load(file)
        if isinstance(transaction_data, list):
            logger.info("Успешный вывод данных с транзакциями")
            return transaction_data
        else:
            logger.error("Данные в файле не являются списком!")
            return []

    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования файла {file_path}")
        return []
