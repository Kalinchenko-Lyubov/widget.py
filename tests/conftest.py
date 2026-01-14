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
