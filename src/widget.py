from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Возвращает строку с замаскированным номером.
    Для карт и счетов используются разные типы маскировки."""
    name = ""
    number = ""
    for symbol in account_card:
        if symbol.isalpha():
            name += symbol
        elif symbol.isdigit():
            number += symbol

    if name != "Счет":
        return f"{name} {get_mask_card_number(number)}"

    else:
        return f"{name} {get_mask_account(number)}"


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


print(get_date("2024-03-11T02:26:18.671407XYZ"))
