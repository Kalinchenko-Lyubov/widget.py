from unittest.mock import mock_open, patch

from src.utils import get_transaction_data


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 1000}]')
def test_get_transaction_data_valid_json(mock_file, mock_exists):
    """Тестируем корректный JSON-файл"""
    result = get_transaction_data("./some/path/data.json")
    assert result == [{"id": 1, "amount": 1000}]


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="{invalid json}")
def test_get_transaction_data_invalid_json(mock_file, mock_exists):
    """Тестируем файл с некорректным JSON"""
    result = get_transaction_data("./some/path/data.json")
    assert result is False


@patch("os.path.exists", return_value=False)
def test_get_transaction_data_no_file(mock_exists):
    """Тестируем случай отсутствия файла"""
    result = get_transaction_data("./some/path/missing.json")
    assert result == []


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_get_transaction_data_not_a_list(mock_file, mock_exists):
    """Тестируем случай, когда данные не являются списком"""
    result = get_transaction_data("./some/path/data.json")
    assert result == []
