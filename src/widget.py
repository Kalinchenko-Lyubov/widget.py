from src.masks import get_mask_account as mask_account
from src.masks import get_mask_card_number as mask_card_number


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
        return f"{name} {mask_card_number(number)}"

    else:
        return f"{name} {mask_account(number)}"
