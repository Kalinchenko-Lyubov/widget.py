import pytest

from src.sort_by_date import sort_by_date


@pytest.mark.parametrize(
    "list_state, result_sort",
    [
        (
            [
                {"date": "2023-01-15", "value": 1},
                {"date": "2024-03-10", "value": 2},
                {"date": "2022-12-01", "value": 3},
            ],
            [
                {"date": "2024-03-10", "value": 2},
                {"date": "2023-01-15", "value": 1},
                {"date": "2022-12-01", "value": 3},
            ],
        ),
        (
            [{"date": "2023-01-15", "value": 1}],
            [
                {"date": "2023-01-15", "value": 1},
            ],
        ),
        (
            [
                {"date": "2024-01-01", "value": 1},
                {"date": "2024-01-01", "value": 2},
                {"date": "2024-01-01", "value": 3},
            ],
            [
                {"date": "2024-01-01", "value": 1},
                {"date": "2024-01-01", "value": 2},
                {"date": "2024-01-01", "value": 3},
            ],
        ),
        (
            [{"date": "2020-02-29", "value": 1}, {"date": "2021-02-28", "value": 2}],
            [{"date": "2021-02-28", "value": 2}, {"date": "2020-02-29", "value": 1}],
        ),
        ([], []),
    ],
)
def test_sort_by_date(list_state, result_sort):
    """Тестируем случаи верного ввода списка с датой"""
    assert sort_by_date(list_state) == result_sort


def test_sort_by_date_list(example_list_in_date):
    """Тестируем случаи верного ввода списка с датой"""
    assert sort_by_date(example_list_in_date) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_ascending():
    """Сортировка по возрастанию (reverse=False)."""
    data = [
        {"date": "2023-01-15", "value": 1},
        {"date": "2024-03-10", "value": 2},
        {"date": "2022-12-01", "value": 3},
    ]
    result = sort_by_date(data, reverse=False)
    assert result[0]["value"] == 3  # 2022-12-01 (самая ранняя)
    assert result[1]["value"] == 1  # 2023-01-15
    assert result[2]["value"] == 2  # 2024-03-10 (самая поздняя)


def test_missing_date_key():
    """Запись без ключа 'date' — должна вызвать KeyError"""
    data = [
        {"value": 1},  # нет 'date'
        {"date": "2024-01-01", "value": 2},
    ]
    with pytest.raises(KeyError):
        sort_by_date(data, reverse=True)


def test_invalid_date_format():
    """Некорректный формат даты"""
    data = [
        {"date": "не-дата", "value": 1},
        {"date": "2024-01-01", "value": 2},
    ]
    with pytest.raises(Exception):  # Можно уточнить тип ошибки
        sort_by_date(data, reverse=True)


def test_empty_date_string():
    """Пустая строка в поле 'date' — вызывает ValueError."""
    data = [{"date": ""}]
    with pytest.raises(ValueError, match="Строка с датой не может быть пустой"):
        sort_by_date(data, reverse=True)
