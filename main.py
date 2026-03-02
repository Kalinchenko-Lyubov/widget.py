import os
from datetime import datetime

from src.file_readers import transactions_from_csv, transactions_from_excel
from src.masks import process_bank_search
from src.processing import filter_by_state
from src.sort_by_date import sort_by_date
from src.utils import get_transaction_data
from src.widget import mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    # Просим пользователя выбрать источник данных
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    choice = input("\nВаш выбор: ")

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        data = get_transaction_data(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "operations.json")
        )
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        data = transactions_from_csv(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "transactions.csv")
        )
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
        data = transactions_from_excel(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "transactions_excel.xlsx")
        )
    else:
        print("Ошибка. Выберите пункт меню: 1, 2 или 3")
        return

    # Проверка наличия данных
    if data is None:
        print("Не удалось загрузить данные. Пожалуйста, проверьте наличие файла и его формат.")
        return

    # Пользователь выбирает статус интересующих его операций
    status = ""
    while status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции '{status}' недоступен. Попробуйте снова")

    # Фильтрация по статусу
    filtered_data = filter_by_state(data, status)
    print(f"Количество транзакций после фильтрации по статусу: {len(filtered_data)}\n")

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice == "да":
        sort_order = input("Отсортировать по возрастанию или по убыванию? (возрастание/убывание): ").strip().lower()
        sorted_data = sort_by_date(filtered_data, reverse=(sort_order != "возрастание"))
    else:
        sorted_data = filtered_data
    print(f"Количество транзакций после сортировки по дате: {len(sorted_data)}\n")

    # Фильтрация по валюте
    rub_only = input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if rub_only == "да":
        if choice == "1":
            # JSON-файл
            sorted_data = [
                trans
                for trans in sorted_data
                if trans.get("operationAmount", {}).get("currency", {}).get("code", "").upper() == "RUB"
            ]
        else:
            # CSV и XLSX-файлы
            sorted_data = [trans for trans in sorted_data if trans.get("currency_code", "").upper() == "RUB"]
    print(f"Количество транзакций после фильтрации по валюте: {len(sorted_data)}\n")

    # Фильтрация по ключевым словам в описании
    word_filter = (
        input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower()
    )
    if word_filter == "да":
        search_term = input("Введите ключевое слово для фильтрации: ")
        sorted_data = process_bank_search(sorted_data, search_term)
    print(f"Количество транзакций после фильтрации по описанию: {len(sorted_data)}\n")

    # Вывод финального отчета
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(sorted_data)}")
    for idx, transaction in enumerate(sorted_data):
        if choice == "1":
            # JSON-файл
            print(
                f"{datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')} "
                f"{transaction.get('description', '')}"
            )
            print(f"{mask_account_card(transaction.get('from'))} -> {mask_account_card(transaction.get('to'))}")
            operation_amount = transaction.get("operationAmount", {})
            currency = operation_amount.get("currency", {}).get("code", "")
            amount = operation_amount.get("amount", "")

            # Вывод суммы без конвертации
            print(f"Сумма: {amount} {currency}\n")
        else:
            # CSV и XLSX-файлы
            print(
                f"{datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d.%m.%Y')} "
                f"{transaction.get('description', '')}"
            )
            print(f"{mask_account_card(transaction.get('from'))} -> {mask_account_card(transaction.get('to'))}")
            currency = transaction.get("currency_code", "")
            amount = transaction.get("amount", "")

            # Вывод суммы без конвертации
            print(f"Сумма: {amount} {currency}\n")

    if not sorted_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
