def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер банковской карты в виде строки без пробелов, возвращает
    маскированный номер карты в формате XXXX XX** **** XXXX"""
    card_number_as_list = [i for i in card_number]
    for i in range(6, 12):
        card_number_as_list[i] = "*"
    masked_card_number = (
        "".join(card_number_as_list[0:4])
        + " "
        + "".join(card_number_as_list[4:8])
        + " "
        + "".join(card_number_as_list[8:12])
        + " "
        + "".join(card_number_as_list[12:16])
    )

    return masked_card_number


def get_mask_account(acc_number: str) -> str:
    """Функция принимает на вход номер счета в виде строки и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки"""
    masked_acc_number = "**" + acc_number[(len(acc_number) - 4) : (len(acc_number) + 1)]
    return masked_acc_number
