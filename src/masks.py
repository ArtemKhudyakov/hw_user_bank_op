import logging
from pathlib import Path

import src.decorators as decorators

current_file_path = Path(__file__).resolve()
project_root_path = current_file_path.parent.parent


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    f"{project_root_path}/logs/masks.log", encoding="utf-8", mode="w"
)
file_formater = logging.Formatter(
    "%(asctime)s - %(name)s -%(funcName)s - %(lineno)d - %(levelname)s -"
    " %(message)s"
)
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


@decorators.log("logs/my_log.txt")
def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер банковской карты в виде строки без пробелов,
    возвращает маскированный номер карты в формате XXXX XX** **** XXXX"""
    logger.debug("Проверяем правильность ввода номера карты")
    if card_number.isdigit() is True and len(card_number) == 16:
        card_number_as_list = [i for i in card_number]
        logger.debug("Маскируем номер карты")
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
    else:
        logger.error("Введен неверный формат номера карты")
        raise ValueError("Неверный формат номера карты")

    logger.debug(
        f"Возвращаем замаскированный номер карты {masked_card_number}"
    )
    return masked_card_number


@decorators.log("logs/my_log.txt")
def get_mask_account(acc_number: str) -> str:
    """Функция принимает на вход номер счета в виде строки и возвращает его
    маску. Номер счета замаскирован и отображается в формате **XXXX,
    где X — это цифра номера. То есть видны только последние 4 цифры номера,
    а перед ними — две звездочки
    """
    logger.debug("Проверяем правильность ввода номера счета")
    if acc_number.isdigit() is True and len(acc_number) == 20:
        logger.debug("Маскируем номер счета")
        masked_acc_number = (
            "**" + acc_number[(len(acc_number) - 4) : (len(acc_number) + 1)]
        )
        logger.debug(
            f"Возвращаем замаскированный номер счета {masked_acc_number}"
        )
        return masked_acc_number
    else:
        logger.error("Введен неверный формат номера счета")
        raise ValueError("Неверный формат номера счета")
