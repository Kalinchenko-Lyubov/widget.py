import pytest

from src.masks import get_mask_account, get_mask_card_number, process_bank_search, process_bank_operations


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
        match="Неверный номер карты. Проверьте количество цифр, их должно быть 16",
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


def test_positive_match(bank_data):
    """Тест на положительный результат"""
    result = process_bank_search(bank_data, "ОПЛАТА")
    assert len(result) == 2
    assert result[0]["id"] == 1

def test_negative_match(bank_data):
    """Тест на отрицательный результат"""
    result = process_bank_search(bank_data, "Недвижимость")
    assert len(result) == 0

def test_empty_description(bank_data):
    """Тест на обработку пустых описаний"""
    result = process_bank_search(bank_data, "")
    assert len(result) == 0

def test_empty_input():
    """Тест на пустой список данных"""
    empty_data = []
    result = process_bank_search(empty_data, "зарплата")
    assert len(result) == 0

def test_partial_word_match(bank_data):
    """Тест на совпадающие части слов"""
    result = process_bank_search(bank_data, "товар")
    assert len(result) == 2
    assert result[0]["id"] == 1


def test_exact_match(bank_data):
    """Тест точного соответствия категории"""
    categories = ["оплата товаров"]
    result = process_bank_operations(bank_data, categories)
    assert result == {"оплата товаров": 2}

def test_non_existing_category(bank_data):
    """Тест на категорию, которой нет среди операций"""
    categories = ["услуги связи"]
    result = process_bank_operations(bank_data, categories)
    assert result == {"услуги связи": 0}

def test_multiple_categories(bank_data):
    """Тест на множественные категории"""
    categories = ["оплата товаров", "комиссия банка", "покупка продуктов"]
    result = process_bank_operations(bank_data, categories)
    assert result == {"оплата товаров": 2, "комиссия банка": 1, "покупка продуктов": 1}

def test_empty_data():
    """Тест на пустой список данных"""
    empty_data = []
    categories = ["оплата товаров"]
    result = process_bank_operations(empty_data, categories)
    assert result == {"оплата товаров": 0}

def test_empty_categories(bank_data):
    """Тест на пустой список категорий"""
    categories = []
    result = process_bank_operations(bank_data, categories)
    assert result == {}
