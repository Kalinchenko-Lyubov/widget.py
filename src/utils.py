import json
import os
from typing import Any, Dict, List
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler = logging.FileHandler('logs.log', encoding='utf-8')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction_data(file_path: str) -> List[Dict[str, Any]] | bool:
    """Возвращает данные о финансовых транзакциях"""
    logger.info('Выполняем проверку наличия информации о финансовых транзакциях')

    if not os.path.exists(file_path):
        logger.warning(f'Файл {file_path} не найден.')
        return []
    try:
        logger.info('Открываем файл с транзакциями')
        with open(file_path, encoding="utf-8") as file:
            transaction_data = json.load(file)
        if isinstance(transaction_data, list):
            logger.info('Успешный вывод данных с транзакциями')
            return transaction_data
        else:
            logger.error('Данные в файле не являются списком!')
            return []

    except json.JSONDecodeError:
        logger.error(f'Ошибка декодирования файла {file_path}')
        return []

    return []


if __name__ == "__main__":
    print(get_transaction_data(os.path.join(os.path.dirname(__file__), '../data/operations.json')))


# Создайте логеры для перечисленных модулей:
# masks,
# utils.
# Реализуйте запись логов в файл. Логи должны записываться в папку
# logs в корне проекта. Файлы логов должны иметь расширение
# .log.
# Формат записи лога в файл должен включать метку времени,
# название модуля, уровень серьезности и сообщение, описывающее
# событие или ошибку, которые произошли.
# Лог должен перезаписываться при каждом запуске приложения.