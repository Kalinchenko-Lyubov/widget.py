import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, mask_account",
    [
        ("Visa Platinum 7000792289606361", "VisaPlatinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_card, mask_account):
    """Тестируем случаи верного ввода номера карты"""
    assert mask_account_card(account_card) == mask_account


@pytest.mark.parametrize(
    "date_string, result",
    [
        ("2025-03-11T02:26:18.671407", "11.03.2025"),
        ("2025-03-11T02:26:18", "11.03.2025"),
        ("2025-01-01T00:00:00", "01.01.2025"),
        ("2025-12-31T23:59:59.999999", "31.12.2025"),
        ("2024-02-29T12:00:00", "29.02.2024"),
        ("2025-02-28T12:00:00", "28.02.2025"),
        ("2024-03-11 02:26:18.671407", "11.03.2024"),
    ],
)
def test_get_date(date_string, result):
    assert get_date(date_string) == result


@pytest.mark.parametrize(
    "date_string",
    [
        ("2024-02-30T00:00:00"),
        ("2024-13-01T00:00:00"),
        ("2024-01-32T00:00:00"),
        ("-0001-01-01T00:00:00"),
        ("2024-01-01T00:60:00"),
        ("2024-01-01T00:00:60"),
        (""),
        ("2024"),
        ("   "),
        ("aaaa bbbb ,."),
    ],
)
def test_get_date_invalid(date_string):
    """Тестируем ошибочные случаи ввода даты"""
    with pytest.raises(ValueError):
        get_date(date_string)
