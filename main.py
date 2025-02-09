import src.masks
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
]

date = "2024-03-11T02:26:18.671407"

for number in data:
    print(src.widjet.mask_account_card(number))

print(src.widjet.get_date(date))