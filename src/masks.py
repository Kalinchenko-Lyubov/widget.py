from typing import Union


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Маскирует номер банковской карты: возвращает первые 6 и последние 4 цифры, между ними *"""

    if len(str(number_card)) != 16:
        raise ValueError("Неверный номер карты. Проверьте количество цифр, их должно быть 16")

    if not str(number_card).isdigit():
        raise ValueError("Номер карты состоит только из цифр")

    mask_card_num = f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"
    return mask_card_num


def get_mask_account(user_account: Union[int, str]) -> str:
    """Маскирует номер банковского счета: принимает число, возвращает ** и 4 последние цифры"""

    if not str(user_account).isdigit():
        raise ValueError("Номер счета состоит только из цифр")

    if len(str(user_account)) < 4:
        raise ValueError("Номер счета должен содержать не менее 4 цифр")

    mask_account = f"**{str(user_account)[-4:]}"
    return mask_account
