import pytest
import pandas as pd


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


@pytest.fixture
def example_transactions():
    return (
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    )


@pytest.fixture
def sample_df():
    """Фиктивный DataFrame для замещения данных"""
    return pd.DataFrame(
        {
            "id": ["1", "2"],
            "state": ["EXECUTED", "CANCELED"],
            "date": ["2023-09-05T11:30:32Z", "2023-09-05T11:30:32Z"],
            "amount": [16210, 29740],
            "currency_name": ["Sol", "Peso"],
            "currency_code": ["PEN", "COP"],
            "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
            "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
            "description": ["Перевод организации", "Перевод с карты на карту"],
        }
    )

@pytest.fixture
def bank_data():
    return [
    {"id": 1, "description": "Оплата товаров"},
    {"id": 2, "description": "Перечисление зарплаты"},
    {"id": 3, "description": "Покупка продуктов"},
    {"id": 4, "description": ""},
    {"id": 5, "description": "Комиссия банка"},
    {"id": 6, "description": "ОплатА товАРОВ"}
]