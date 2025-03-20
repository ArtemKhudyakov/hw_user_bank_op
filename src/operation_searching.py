import re
from collections import Counter, defaultdict

from pyflakes.checker import counter
from unicodedata import category

from src.data_reader import xlsx_reader

operations_list = xlsx_reader('data/transactions_excel.xlsx')
#     [
#     {
#         "id": 650703.0,
#         "state": "EXECUTED",
#         "date": "2023-09-05T11:30:32Z",
#         "amount": 16210.0,
#         "currency_name": "Sol",
#         "currency_code": "PEN",
#         "from": "Счет 58803664561298323391",
#         "to": "Счет 39745660563456619397",
#         "description": "Перевод организации",
#     },
#     {
#         "id": 3598919.0,
#         "state": "EXECUTED",
#         "date": "2020-12-06T23:00:58Z",
#         "amount": 29740.0,
#         "currency_name": "Peso",
#         "currency_code": "COP",
#         "from": "Discover 3172601889670065",
#         "to": "Discover 0720428384694643",
#         "description": "Перевод с карты на карту",
#     },
#     {
#         "id": 593027.0,
#         "state": "CANCELED",
#         "date": "2023-07-22T05:02:01Z",
#         "amount": 30368.0,
#         "currency_name": "Shilling",
#         "currency_code": "TZS",
#         "from": "Visa 1959232722494097",
#         "to": "Visa 6804119550473710",
#         "description": "Перевод с карты на карту",
#     },
# ]


def op_searching_by_description(
        string_for_searching: str, operations_list: list[dict[str, str]]
) -> list[dict[str, str]]:
    """Принимает список словарей с данными о банковских операциях и строку поиска, а возвращать список словарей,
у которых в описании есть данная строка."""
    operations_by_description = [
        operation
        for operation in operations_list
        if re.search(string_for_searching, operation["description"], re.IGNORECASE)
    ]
    return operations_by_description

srch_categories_list = ['Открытие вклада', 'Перевод с карты на карту']
# принимать список словарей с данными о банковских операциях и список категорий операций, а возвращать словарь, в
# котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
def op_counter_by_category(operations_list: list[dict[str, str]], srch_categories_list=None):
    srch_counter = dict()
    op_category_list = [operation["description"] for operation in operations_list]
    category_counter = Counter(op_category_list)

    for i in srch_categories_list:
        if i in op_category_list:
            for k, v in category_counter.items():
                if k in srch_categories_list:
                    srch_counter[k] = v
        else:
            srch_counter[i] = "операция не найдена"
    print(category_counter)
    print(srch_counter)


op_counter_by_category(operations_list, srch_categories_list)