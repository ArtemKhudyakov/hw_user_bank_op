import src.masks
import src.processing
import src.widjet

card_number: str = str(7000792289606361)
acc_number: str = str(73654108430135874305)
masked_card_number: str = src.masks.get_mask_card_number(card_number)
masked_acc_number: str = src.masks.get_mask_account(acc_number)
print(masked_card_number)
print(masked_acc_number)
print()

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
    'fdsf',
    ''
]

dates = ["2024-03-11T02:26:18.671407", "2025-12-11T02:26:18.671407", '', 'Error']

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

for number in data:
    try:
        print(src.widjet.mask_account_card(number))
    except ValueError:
        print ("Input error")

print()
for date in dates:
    try:
        print(src.widjet.get_date(date))
    except ValueError:
        print ("Input error")

print()
for operation in src.processing.filter_by_state(operations_data):
    print(operation)
print()
sorted_operations = src.processing.sort_by_date(operations_data)
for operation in sorted_operations:
    print(operation)
print()
for operation in src.processing.sort_by_date(
    src.processing.filter_by_state(operations_data), False
):
    print(operation)
