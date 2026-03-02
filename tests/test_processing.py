from src.processing import filter_by_state


def test_filter_by_state_ex(example_list_in_date):
    """Тестируем случаи верного ввода списка со state=EXECUTED"""
    assert filter_by_state(example_list_in_date, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_cancel(example_list_in_date):
    """Тестируем случаи верного ввода списка со state=CANCELED"""
    assert filter_by_state(example_list_in_date, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_non_existent():
    """Тест: нет элементов с заданным state"""
    list_state = [{"id": 1, "state": "PENDING"}, {"id": 2, "state": "CANCELLED"}]
    assert filter_by_state(list_state, state="CANCELED") == []


def test_filter_by_empty_list():
    """Тест: пустая входная последовательность"""
    assert filter_by_state([], state="EXECUTED") == []


def test_filter_by_missing_state():
    """Тест: пропуск транзакций без состояния"""
    list_state = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2},
        {"id": 3, "state": "CANCELED"},
        {"id": 4},
    ]
    assert filter_by_state(list_state, state="EXECUTED") == [{"id": 1, "state": "EXECUTED"}]


def test_filter_by_case_insensitive():
    """Тест: чувствительность к регистру"""
    list_state = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "executed"},
        {"id": 3, "state": "CANCELED"},
    ]
    assert filter_by_state(list_state, state="EXECUTED") == [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "executed"},
    ]
