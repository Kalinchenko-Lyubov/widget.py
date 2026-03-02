def filter_by_state(list_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Возвращает список словарей с указанным значением ключа state.
    Контролирует количество пропущенных транзакций.
    """
    result = []
    skipped_count = 0

    for el in list_state:
        current_state = str(el.get("state", ""))
        if not current_state:
            skipped_count += 1
            continue  # Пропускаем транзакции без состояния

        if current_state.upper() == state.upper():
            result.append(el)

    if skipped_count > 0:
        print(f"Предупреждение: пропущено {skipped_count} транзакций без состояния.")

    return result
