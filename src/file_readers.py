import pandas as pd
import os


def transactions_from_csv(path_file_csv):
    """Функция принимает путь CSV-файла и возвращает список словарей
    с данными по банковским транзакциям"""
    try:
        df = pd.read_csv(path_file_csv, sep=';', engine='python')
        transactions = df.to_dict(orient="records")

        return transactions
    except FileNotFoundError:
        print(f"Файл {path_file_csv} не найден.")
    except pd.errors.EmptyDataError:
        print(f"В файле {path_file_csv} нет данных.")
    except pd.errors.ParserError:
        print(f"Ошибка при разборе файла {path_file_csv}. Возможно, неверный формат.")
    except Exception as ex:
        print(f"Общая ошибка: {ex}")


def transactions_from_exel(path_file_excel):
    """Функция принимает путь к XLSX-файлу и возвращает
    списки словарей с данными по банковским транзакциям"""
    try:
        df = pd.read_excel(path_file_excel)
        transactions = df.to_dict(orient='records')

        return transactions

    except FileNotFoundError:
        print(f"Файл {path_file_excel} не найден.")
    except pd.errors.EmptyDataError:
        print(f"В файле {path_file_excel} нет данных.")
    except pd.errors.ParserError:
        print(f"Ошибка при разборе файла {path_file_excel}. Возможно, неверный формат.")
    except Exception as ex:
        print(f"Общая ошибка: {ex}")

if __name__ == "__main__":
    print(transactions_from_exel(os.path.join(os.path.dirname(__file__), "../data/transactions_excel.xlsx")))
