import src.masks
import src.processing
import src.widjet
import src.generators as gen

# card_number: str = str(7000792289606361)
# acc_number: str = str(73654108430135874305)
# masked_card_number: str = src.masks.get_mask_card_number(card_number)
# masked_acc_number: str = src.masks.get_mask_account(acc_number)
# print(masked_card_number)
# print(masked_acc_number)
# print()

data = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
    "Visa Gold 5999414228426",
    "fdsf",
    "",
]

dates = [
    "2024-03-11T02:26:18.671407",
    "2025-12-11T02:26:18.671407",
    "",
    "Error",
]

operations_data = [
    {
        "id": "41428829",
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
    },
    {
        "id": "939719570",
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
    },
    {
        "id": "594226727",
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
    },
    {
        "id": "615064591",
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
    },
]

transactions = [
    {
        "id": "939719570",
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": "142264268",
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": "873106923",
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": "895315941",
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": "594226727",
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


# for number in data:
#     try:
#         print(src.widjet.mask_account_card(number))
#     except ValueError:
#         print("Input error")



# print()
# for date in dates:
#     try:
#         print(src.widjet.get_date(date))
#     except ValueError:
#         print("Input error")
#
# print()
#
# try:
#     for operation in src.processing.filter_by_state(operations_data):
#         try:
#             print(operation)
#         except ValueError:
#             print("Input error")
# except ValueError:
#     print("Input error")
#
# print()
#
# sorted_operations = src.processing.sort_by_date(operations_data)
# for operation in sorted_operations:
#     print(operation)
# print()
# for operation in src.processing.sort_by_date(
#     src.processing.filter_by_state(operations_data), False
# ):
#     print(operation)
#
#


currency = input("Введите валюту для фильтрации (RUB, USD, EUR)").upper()
#
# # print("Проверка filter_by_currency")
# # try:
# #     usd_transactions = gen.filter_by_currency(transactions, currency)
# #     if not list(usd_transactions):
# #         print("Транзакции в данной валюте не производились")
# #     else:
# #         usd_transactions = gen.filter_by_currency(transactions, currency)
# #         print(list(usd_transactions))
# # except ValueError:
# #     print("Список транзакций пуст")
# #
# print("####")
# print("Проверка filter_by_currency, если список пустой")
#
# try:
#     usd_transactions = gen.filter_by_currency([])
#     if not list(usd_transactions):
#         print("Транзакции в данной валюте не производились")
#     else:
#         usd_transactions = gen.filter_by_currency([])
#         print(list(usd_transactions))
# except ValueError:
#     print("Список транзакций пуст")
#
# print("#####")
# print("Проверка transaction_descriptions")
#
# try:
#     description = gen.transaction_descriptions(transactions)
#     print(next(description))
#     print(next(description))
#
#     description = gen.transaction_descriptions([])
#     print(next(description))
# except ValueError:
#     print("Список транзакций пуст")
#
print("####")
print(
    "Проверка transaction_descriptions после фильтрации"
    " функцией filter_by_currency"
)

try:
    filtered = list(gen.filter_by_currency(transactions, currency))
    filtered_descriptions = gen.transaction_descriptions(filtered)
    for _ in range(len(filtered)):
        print(next(filtered_descriptions))
except StopIteration:
    print("Транзакции закончились")

except ValueError:
    print("Список транзакций пуст")

# print("####")
# print("Проверка card_number_generator")


# card_numbers = gen.card_number_generator(1, 10000000)
# try:
#     for i in range(1000000):
#         print(next(card_numbers))
# except StopIteration:
#     print("Хватит уже")


