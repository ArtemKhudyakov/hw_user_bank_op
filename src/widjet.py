def mask_account_card(input_data: str) -> str:
    """Функция принимает номер счет в формате
    "Счет 73654108430135874305" или номер карты в формате
    "MasterCard 7158300734726758" или "Visa Platinum 7000792289606361"
    и возвращет скрытый номер счета в формате "Счет **4305" или карты
    в формате "Visa Platinum 7000 79** **** 6361".
    """
    import src.masks

    splited_input_data: list = input_data.split()

    if len(splited_input_data) > 0:
        if len(splited_input_data[-1]) == 20:
            masked_acc: str = src.masks.get_mask_account(splited_input_data[-1])
            splited_masked_acc: list = [
                i for i in splited_input_data if not i.isdigit()
            ]
            splited_masked_acc.append(masked_acc)
            return " ".join(splited_masked_acc)

        elif len(splited_input_data[-1]) == 16:
            masked_card: str = src.masks.get_mask_card_number(
                splited_input_data[-1]
            )
            splited_masked_card: list = [
                i for i in splited_input_data if not i.isdigit()
            ]
            splited_masked_card.append(masked_card)
            return " ".join(splited_masked_card)

        else:
            raise ValueError("Input error")
    else:
        raise ValueError("Input error")


def get_date(date: str) -> str:
    """Функция принимает дату в формате "2024-03-11T02:26:18.671407"
    и возвращает дату в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""

    date_as_dict: dict = {"year": "", "month": "", "day": ""}
    if len(date) != 0:
        for char in date:
            if char.isdigit() and len(date_as_dict["year"]) < 4:
                date_as_dict["year"] += char
            elif char.isdigit() and len(date_as_dict["month"]) < 2:
                date_as_dict["month"] += char
            elif char.isdigit() and len(date_as_dict["day"]) < 2:
                date_as_dict["day"] += char
        for v in date_as_dict.values():
            if not v.isdigit():
                raise ValueError("Input error")
            else:
                transformated_date = (
                    f"{date_as_dict['day']}.{date_as_dict['month']}.{date_as_dict['year']}"
                )
            return transformated_date
    else:
        raise ValueError("Input error")
