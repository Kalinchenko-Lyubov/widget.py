from typing import Any, Hashable

import pandas as pd


def transactions_from_csv(path_file_csv: str) -> list[dict[Hashable, Any]] | None:
    """Функция принимает путь CSV-файла и возвращает список словарей
    с данными по банковским транзакциям"""
    try:
        df = pd.read_csv(path_file_csv, sep=";", engine="python")
        transactions = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError:
        print(f"Файл {path_file_csv} не найден.")
        return None
    except pd.errors.EmptyDataError:
        print(f"В файле {path_file_csv} нет данных.")
        return None
    except pd.errors.ParserError:
        print(f"Ошибка при разборе файла {path_file_csv}. Возможно, неверный формат.")
        return None
    except Exception as ex:
        print(f"Общая ошибка: {ex}")
        return None


def transactions_from_excel(path_file_excel: str) -> list[dict[Hashable, Any]] | None:
    """Функция принимает путь к XLSX-файлу и возвращает
    списки словарей с данными по банковским транзакциям"""
    try:
        df = pd.read_excel(path_file_excel)
        transactions = df.to_dict(orient="records")

        return transactions

    except FileNotFoundError:
        print(f"Файл {path_file_excel} не найден.")
        return None
    except pd.errors.EmptyDataError:
        print(f"В файле {path_file_excel} нет данных.")
        return None
    except pd.errors.ParserError:
        print(f"Ошибка при разборе файла {path_file_excel}. Возможно, неверный формат.")
        return None
    except Exception as ex:
        print(f"Общая ошибка: {ex}")
        return None
