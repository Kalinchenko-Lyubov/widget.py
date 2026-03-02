from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card):
    """Возвращает строку с замаскированным номером.
    Для карт и счетов используются разные типы маскировки."""
    if not isinstance(account_card, str):  # Проверка, что данные являются строкой
        return "Ошибка: данные не являются строкой"

    if not account_card:  # Проверка на None или пустую строку
        return "Данные отсутствуют"

    name = ""
    number = ""
    for symbol in account_card:
        if symbol.isalpha() or symbol == " ":
            name += symbol
        elif symbol.isdigit():
            number += symbol

    if "Счет" not in name:
        return f"{name}{get_mask_card_number(number.replace(' ', ''))}"
    else:
        return f"{name}{get_mask_account(number.replace(' ', ''))}"


def get_date(date_string: str) -> str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" """

    date_string = date_string.strip()  # Удаляем пробелы в начале и конце строки (если есть)

    if not date_string:  # Проверяем, что строка не пустая
        raise ValueError("Строка с датой не может быть пустой")

    try:
        dt = datetime.fromisoformat(date_string)  # Преобразуем строку в объект datetime

        return dt.strftime("%d.%m.%Y")  # Формируем результат в нужном формате

    except ValueError as e:
        # Перехватываем ошибки формата/некорректных данных
        raise ValueError(f"Неверный формат даты или некорректные данные: {e}")
