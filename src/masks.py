import logging
import os
import re
from collections import Counter
from typing import Dict, List, Union

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks_logs.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Маскирует номер банковской карты: возвращает первые 6 и последние 4 цифры, между ними *"""

    logger.info("Приступаем к маскировке банковской карты")
    if len(str(number_card)) != 16:
        logger.error("Ошибка введения данных: введено неверное количество цифр")
        raise ValueError("Неверный номер карты. Проверьте количество цифр, их должно быть 16")

    if not str(number_card).isdigit():
        logger.error("Ошибка введения данных: введены неверные символы")
        raise ValueError("Номер карты состоит только из цифр")

    mask_card_num = f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"
    logger.info("Успешное выполнение маскировки банковской карты")
    return mask_card_num


def get_mask_account(user_account: Union[int, str]) -> str:
    """Маскирует номер банковского счета: принимает число, возвращает ** и 4 последние цифры"""

    logger.info("Приступаем к маскировке банковского счета")
    if not str(user_account).isdigit():
        logger.error("Ошибка введения данных: введены неверные символы")
        raise ValueError("Номер счета состоит только из цифр")

    if len(str(user_account)) < 4:
        logger.error("Ошибка введения данных: введено неверное количество цифр")
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    mask_account = f"**{str(user_account)[-4:]}"
    logger.info("Успешное выполнение маскировки банковского счета")
    return mask_account


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Регулярное выражение, которое ищет строку поиска без учета регистра символов"""
    if not search.strip():
        return []

    pattern = re.compile(search, re.IGNORECASE)
    result = [item for item in data if "description" in item and pattern.search(item["description"])]

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Функция подсчитывает количество операций по заданным категориям"""
    all_descriptions = [op.get("description", "").lower().strip() for op in data]

    count = Counter(all_descriptions)

    result = {}
    for cat in categories:
        normalized_cat = cat.lower().strip()
        result[normalized_cat] = count.get(normalized_cat.lower(), 0)

    return result
