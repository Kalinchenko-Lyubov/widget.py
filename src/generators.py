from typing import Iterator, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции по ключу currency"""
    if len(transactions) == 0:
        raise ValueError("Введите данные операции")

    transactions_cur = [x for x in transactions if x["operationAmount"]["currency"]["code"] == currency]
    for transaction in transactions_cur:
        yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Функция возвращает описание каждой операции по очереди"""
    if len(transactions) == 0:
        raise ValueError("Введите данные операции")

    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    if start < 0:
        raise ValueError("Начальное значение не должно быть отрицательным")
    if stop < start:
        raise ValueError("Конечное значение не должно быть меньше начального")
    if start > 9999999999999999 or stop > 9999999999999999:
        raise ValueError("Значения должны быть не более 9999999999999999")

    for num in range(start, stop + 1):
        # Формируем 16‑значное число с ведущими нулями
        num_str = f"{num:016d}"
        # Разбиваем на блоки по 4 цифры через пробелы
        formatted_number = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
        yield formatted_number
