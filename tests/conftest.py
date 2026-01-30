import pytest


@pytest.fixture
def example_num_card_invalid():
    return [
        "aaaabbbbccccdddd",
        "ааааббббввввгггг",
        'a ,."%#@!&*()/*[]{}',
        "111122223333",
        "11112222333344445555",
        "",
        " ",
        "123фыв123 asd-",
        "111122223333asfg",
        "123",
        "123фыв123 asd-",
        "1111-2222-3333-as-fg",
    ]


@pytest.fixture
def example_num_account_invalid():
    return [
        "aaaabbbbccccdddd",
        "ааааббббввввгггг",
        'a ,."%#@!&*()/*[]{}',
        "",
        " ",
        "123фыв123 asd-",
        "111122223333asfg",
        "123",
        "123фыв123 asd-",
        "1111-2222-3333-as-fg",
    ]


@pytest.fixture
def example_list_in_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
