import pytest

from src.masks import get_mask_card_number, get_mask_account
from tests.coverage import example_num_card_invalid, example_num_account_invalid


@pytest.mark.parametrize(
    "number_card, mask_card",
    [("1111222233334444", "1111 22** **** 4444"), ("0000000000000000", "0000 00** **** 0000")],
)
def test_get_mask_card_number(number_card, mask_card):
    """Тестируем случаи верного ввода номера карты"""
    assert get_mask_card_number(number_card) == mask_card


def test_get_mask_card_number_invalid(example_num_card_invalid):
    """Тестируем ошибочные случаи ввода номера карты"""
    for num_card in example_num_card_invalid:
        with pytest.raises(ValueError):
            get_mask_card_number(num_card)


def test_get_mask_card_number_letters(number_card="123фыв123 asd-"):
    """Проверяем, правильность сообщения об ошибке"""
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


def test_get_mask_account_invalid(example_num_account_invalid):
    """Тестируем ошибочные случаи ввода номера счета"""
    for num_account in example_num_account_invalid:
        with pytest.raises(ValueError):
            get_mask_account(num_account)


def test_get_mask_account_letters(user_account="123 фыв 123 asd- 1234"):
    """Проверяем, правильность сообщения об ошибке"""
    with pytest.raises(
        ValueError,
        match="Номер счета состоит только из цифр",
    ):
        get_mask_account(user_account)
