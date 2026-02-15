from unittest.mock import Mock, patch

import pytest

from src.external_api import get_sum_transaction_rub


def test_get_sum_transaction_rub():
    """Тестируем успешную операцию с currency = RUB"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }

    result = get_sum_transaction_rub(transaction)
    assert result == 31957.58


@patch("src.external_api.requests.get")
def test_get_sum_transaction_rub_from_usd(mock_request):
    """Тестируем успешную операцию с currency = USD"""
    mock_request.return_value = Mock(status_code=200, json=lambda: {"result": 8221.37})
    transaction = {
        "id": 41428829,
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert get_sum_transaction_rub(transaction) == 8221.37


def test_get_sum_transaction_rub_empty_transaction():
    """Тестируем поведение при пустой транзакции"""
    transaction = {}
    result = get_sum_transaction_rub(transaction)
    assert result is None


def test_get_sum_transaction_rub_invalid_structure():
    """Тестируем поведение при отсутствующих полях"""
    transaction = {"id": 441945886, "operationAmount": {"amount": "31957.58"}}

    with pytest.raises(ValueError):
        get_sum_transaction_rub(transaction)


@patch("src.external_api.requests.get")
def test_get_sum_transaction_rub_conversion_error(mock_request):
    """Тестируем ошибку конвертации"""
    mock_request.return_value = Mock(status_code=400, json=lambda: {})

    transaction = {
        "id": 41428829,
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    }

    with pytest.raises(Exception):
        get_sum_transaction_rub(transaction)
