import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(example_transactions):
    """Фильтрация по USD"""
    result = list(filter_by_currency(example_transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_no_matches(example_transactions):
    """Фильтрация по несуществующей валюте"""
    result = list(filter_by_currency(example_transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty_list():
    """Пустой список транзакций"""
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency([], "USD"))
    assert "Введите данные операции" in str(exc_info.value)


def test_transaction_descriptions_success(example_transactions):
    """Получение описаний"""
    result = list(transaction_descriptions(example_transactions))
    assert len(result) == 2
    assert result[0] == "Перевод организации"
    assert result[1] == "Перевод со счета на счет"


def test_transaction_descriptions_empty_list():
    """Пустой список транзакций"""
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions([]))
    assert "Введите данные операции" in str(exc_info.value)


def test_transaction_descriptions_missing_description():
    """Транзакция без description"""
    transaction_without_desc = {
        "id": 1,
        "state": "EXECUTED",
        "date": "2023-01-01T00:00:00",
        "operationAmount": {"amount": "100.00", "currency": {"name": "RUB", "code": "RUB"}},
        # description отсутствует!
        "from": "Счет 123",
        "to": "Счет 456",
    }
    transactions = [transaction_without_desc]

    result = list(transaction_descriptions(transactions))
    assert len(result) == 0


def test_transaction_descriptions_mixed(example_transactions):
    """Смешанные транзакции. Добавляем транзакцию без description к существующим"""
    bad_transaction = {
        "id": 999,
        "state": "EXECUTED",
        "date": "2023-01-02T00:00:00",
        "operationAmount": {"amount": "500.00", "currency": {"name": "EUR", "code": "EUR"}},
    }
    mixed_transactions = list(example_transactions) + [bad_transaction]

    result = list(transaction_descriptions(mixed_transactions))
    assert len(result) == 2
    assert "Перевод организации" in result
    assert "Перевод со счета на счет" in result


def test_transaction_descriptions_iterator(example_transactions):
    """Проверка итератора"""
    iterator = transaction_descriptions(example_transactions)

    first = next(iterator)
    assert first == "Перевод организации"

    second = next(iterator)
    assert second == "Перевод со счета на счет"

    with pytest.raises(StopIteration):
        next(iterator)


@pytest.mark.parametrize(
    ("start", "stop", "expected"),
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1000, 1000, ["0000 0000 0000 1000"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (999999, 1000001, ["0000 0000 0099 9999", "0000 0000 0100 0000", "0000 0000 0100 0001"]),
    ],
)
def test_card_number_generator_valid_ranges(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_format():
    result = list(card_number_generator(12345678, 12345678))
    parts = result[0].split()
    assert len(parts) == 4
    assert all(len(part) == 4 and part.isdigit() for part in parts)


def test_card_number_generator_negative_start():
    with pytest.raises(ValueError, match="Начальное значение не должно быть отрицательным"):
        list(card_number_generator(-1, 5))


def test_card_number_generator_stop_less_than_start():
    with pytest.raises(ValueError, match="Конечное значение не должно быть меньше начального"):
        list(card_number_generator(10, 5))


def test_card_number_generator_exceeds_max():
    with pytest.raises(ValueError, match="Значения должны быть не более 9999999999999999"):
        list(card_number_generator(10**16, 10**16))
