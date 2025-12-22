def get_mask_card_number(number_card: int) -> str:
    """Маскирует номер банковской карты: возвращает первые 6 и последние 4 цифры, между ними *"""
    mask_card_num = f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"
    return mask_card_num


def get_mask_account(user_account: int) -> str:
    """Маскирует номер банковского счета: принимает число, возвращает ** и 4 последние цифры"""
    mask_account = f"**{str(user_account)[-4:]}"
    return mask_account
