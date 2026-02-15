import json
from unittest.mock import mock_open, patch

from src.utils import get_transaction_data


def test_valid_json():
    """Тестирует успешное чтение корректного JSON-файла"""
    with (
        patch("os.path.exists", return_value=True),
        patch(
            "src.utils.open",
            new_callable=mock_open,
            read_data=json.dumps([{"id": 441945886, "amount": "31957.58"}, {"id": 41428829, "amount": "8221.37"}]),
        ),
    ):
        result = get_transaction_data("./data/transactions.json")
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {"id": 441945886, "amount": "31957.58"}
    assert result[1] == {"id": 41428829, "amount": "8221.37"}


def test_non_existent_file():
    """Тестирование попытки прочитать несуществующий файл"""
    with patch("os.path.exists", return_value=False):
        result = get_transaction_data("./data/non_existent.json")
        assert result == []
        assert isinstance(result, list)


def test_incorrect_json():
    """Тестирование функции с некорректным JSON"""
    with (
        patch("os.path.exists", return_value=True),
        patch("builtins.open", new_callable=mock_open, read_data='{ "id": 1, "amount": }'),
    ):
        result = get_transaction_data("./data/invalid.json")
        assert result is False


def test_empty_file():
    """Тестирует реакцию на пустой файл"""
    empty_data = ""
    with patch("builtins.open", mock_open(read_data=empty_data)):
        result = get_transaction_data("./some/path/empty_file.json")
    assert result == []


def test_not_a_list():
    """Тестирует случай, когда JSON-данные не список"""
    non_list_data = '{"key": "value"}'
    with patch("builtins.open", mock_open(read_data=non_list_data)):
        result = get_transaction_data("./some/path/incorrect_data.json")
    assert result == []
