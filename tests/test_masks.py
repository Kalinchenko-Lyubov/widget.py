import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number_card, mask_card",
    [("1111222233334444", "1111 22** **** 4444"), ("0000000000000000", "0000 00** **** 0000")],
)
def test_get_mask_card_number(number_card, mask_card):
    assert get_mask_card_number(number_card) == mask_card


@pytest.mark.parametrize(
    "number_card",
    [
        "aaaabbbbccccdddd",
        "ааааббббввввгггг",
        'a ,."%#@!&*()/*[]{}',
        "111122223333",
        "11112222333344445555",
        "",
        " ",
        "123фыв123 asd-",
        "111122223333asfg",
    ],
)
def test_get_mask_card_number_invalid(number_card):
    with pytest.raises(ValueError):
        get_mask_card_number(number_card)


def test_get_mask_card_number_letters(number_card="123фыв123 asd-"):
    with pytest.raises(
        ValueError,
        match="Неверный номер карты. Проверьте количество цифр, их должно быть 16.\n"
        "Номер карты состоит только из цифр. Введите все цифры без пробелов и символов",
    ):
        get_mask_card_number(number_card)


@pytest.mark.parametrize(
    "user_account, mask_account",
    [("111122223333444455555", "**5555"), ("73654108430135874305", "**4305"), ("00000000000000000000", "**0000")],
)
def test_get_mask_account(user_account, mask_account):
    assert get_mask_account(user_account) == mask_account


@pytest.mark.parametrize(
    "user_account",
    [
        "aaaabbbbccccddddeeee",
        "ааааббббввввггггдддд",
        "a ,.'%#@!&*()/*[]{}",
        "",
        "123",
        " "
        "123фыв123 asd-",
        "1111-2222-3333-as-fg",
    ],
)
def test_get_mask_account_invalid(user_account):
    with pytest.raises(ValueError):
        get_mask_account(user_account)


def test_get_mask_account_letters(user_account="123 фыв 123 asd- 1234"):
    with pytest.raises(
        ValueError,
        match="Номер счета состоит только из цифр",
    ):
        get_mask_account(user_account)
