from typing import Any, Collection, Iterator

import src.decorators as decorators

# from typing import TypeGuard
# from typing import Any


@decorators.log("logs/my_log.txt")
def filter_by_currency(
    transactions: list[dict[str, Collection[str]]], currency: str = "USD"
) -> Iterator[dict[str, Collection]]:
    """Функция, которая принимает на вход список словарей, представляющих
    транзакции. Функция возвращает итератор, который поочередно выдает
    транзакции, где валюта операции соответствует заданной (по умолчанию USD).
    """
    if len(transactions) == 0:
        raise ValueError("Список транзакций пуст")
    else:
        filtered_transaction: Iterator[dict[str, Collection[Any]]] = filter(
            lambda x: x["operationAmount"]["currency"]["code"] == currency,
            transactions,
        )
        for transaction in filtered_transaction:
            yield transaction


@decorators.log("logs/my_log.txt")
def transaction_descriptions(
    transactions: list[dict[str, Collection[str]]],
) -> Iterator[Collection[str]]:
    """Генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди."""
    if len(transactions) == 0:
        raise ValueError("Список транзакций пуст")
    else:
        for i in range(len(transactions)):
            yield transactions[i]["description"]


@decorators.log("logs/my_log.txt")
def card_number_generator(
    start: int = 1, stop: int = 9999999999999998
) -> Iterator[str]:
    """Генератор номера карты, который выдает номера банковских
    карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор
    может сгенерировать номера карт в заданном диапазоне от
    0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for i in range(start, stop + 1):
        number = i
        card_number = "".join(
            ([i for i in str(number)[::-1] + "0" * (16 - len(str(number)))])[
                ::-1
            ]
        )
        card_number = (
            card_number[0:4]
            + " "
            + card_number[4:8]
            + " "
            + card_number[8:12]
            + " "
            + card_number[12:]
        )
        yield card_number
        number += 1
