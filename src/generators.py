def filter_by_currency(transactions, currency):
    """Перебираем словари по ключу currency"""
    if len(transactions) == 0:
        raise ValueError("Введите данные операции")

    result = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    for transaction in result:
        yield transaction


transactions = {"id": 939719570,"state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {
              "amount": "9824.07", "currency": {"name": "USD", "code": "USD"}
          }, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"
      }, {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
                             {"amount": "79114.93", "currency": {"name": "USD", "code": "ESD"}},
          "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"}

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))
