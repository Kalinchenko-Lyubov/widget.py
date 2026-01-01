def sort_by_date(list_state: list[dict], reverse: bool = True) -> list[dict]:
    """Сортировка списка словарей по дате"""

    return sorted(list_state, key=lambda x: x["date"], reverse=reverse)
