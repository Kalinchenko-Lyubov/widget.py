from datetime import datetime

from src.widget import get_date


def sort_by_date(list_state: list[dict], reverse: bool = True) -> list[dict]:
    """Сортировка списка словарей по дате"""
    for item in list_state:
        if "date" not in item:
            raise KeyError(f"Словарь не содержит ключа 'date': {item}")

        # Валидируем формат даты через get_date() (вызовет исключение при ошибке)
        get_date(item["date"])

    return sorted(list_state, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
