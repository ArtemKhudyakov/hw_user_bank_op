import src.masks

card_number: str = str(7000792289606361)
acc_number: str = str(73654108430135874305)
masked_card_number: str = src.masks.get_mask_card_number(card_number)
masked_acc_number: str = src.masks.get_mask_account(acc_number)
print(masked_card_number)
print(masked_acc_number)