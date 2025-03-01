from typing import Collection
from functools import wraps
import pytest

import src.generators as gen


def test_filter_by_currency_usd(
    list_of_transactions: list[dict[str, Collection[str]]],
    currency: str = "USD",
) -> None:
    """Тестирование функции filter_by_currency, фильтрация по валюте USD
    тестирование через next"""
    filter_by_currency_usd = gen.filter_by_currency.__wrapped__(
        list_of_transactions, currency
    )

    assert next(filter_by_currency_usd) == list_of_transactions[0]
    assert next(filter_by_currency_usd) == list_of_transactions[1]
    assert next(filter_by_currency_usd) == list_of_transactions[3]


def test_filter_by_currency_all(
    list_of_transactions: list[dict[str, Collection[str]]],
    transactions_by_usd: list[dict[str, Collection[str]]],
    currency: str = "USD",
) -> None:
    """Тестирование функции filter_by_currency по валюте USD, тестирование
    через список"""
    filter_by_currency_usd = gen.filter_by_currency.__wrapped__(
        list_of_transactions, currency
    )
    assert list(filter_by_currency_usd) == transactions_by_usd


def test_filter_by_currency_rub(
    list_of_transactions: list[dict[str, Collection[str]]],
    transactions_by_rub: list[dict[str, Collection[str]]],
    currency: str = "RUB",
) -> None:
    """Тестирование функции filter_by_currency по валюте RUB, тестирование
    через список"""
    filter_by_currency_rub = gen.filter_by_currency.__wrapped__(
        list_of_transactions, currency
    )
    assert list(filter_by_currency_rub) == transactions_by_rub


def test_filter_by_currency_empty(
    transactions: list = [], currency: str = "USD"
) -> None:
    """Тестирование функции filter_by_currency по валюте, тестирование
    пустого списка"""
    with pytest.raises(ValueError):
        assert list(gen.filter_by_currency.__wrapped__(transactions, currency))


def test_filter_by_currency_without_usd(
    transactions_by_rub: list[dict[str, Collection[str]]],
    currency: str = "USD",
) -> None:
    """Тестирование функции filter_by_currency по валюте USD, тестирование
    списка транзакций, не содержащего операций в USD"""
    assert list(gen.filter_by_currency.__wrapped__(transactions_by_rub, currency)) == []


def test_filter_by_currency_eur(
    list_of_transactions: list[dict[str, Collection[str]]],
    currency: str = "EUR",
) -> None:
    """Тестирование функции filter_by_currency по валюте EUR, тестирование
    списка транзакций, не содержащего операций в EUR"""
    assert list(gen.filter_by_currency.__wrapped__(list_of_transactions, currency)) == []


def test_transaction_descriptions(
    list_of_transactions: list[dict[str, Collection[str]]],
) -> None:
    """Тестирование функции transaction_descriptions,
    тестирование через next"""
    description = gen.transaction_descriptions.__wrapped__(list_of_transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


def test_transaction_descriptions_empty(transactions: list = []) -> None:
    """Тестирование функции transaction_descriptions, если список транзакций
    пуст"""
    with pytest.raises(ValueError):
        assert next(gen.transaction_descriptions.__wrapped__(transactions)) == ""


def test_transaction_descriptions_with_filter_rub(
    list_of_transactions: list[dict[str, Collection[str]]],
) -> None:
    """Тестирование функции transaction_descriptions, после фильтрации
    по валюте RUB"""
    filtered = gen.filter_by_currency.__wrapped__(list_of_transactions, "RUB")
    filtered_descriptions = gen.transaction_descriptions.__wrapped__(list(filtered))
    assert list(filtered_descriptions) == [
        "Перевод со счета на счет",
        "Перевод организации",
    ]


def test_transaction_descriptions_with_filter_eur(
    list_of_transactions: list[dict[str, Collection[str]]],
) -> None:
    """Тестирование функции transaction_descriptions, после фильтрации
    по валюте EUR, если в отфильтрованном списке нет операций"""
    filtered = gen.filter_by_currency.__wrapped__(list_of_transactions, "EUR")
    filtered_descriptions = gen.transaction_descriptions.__wrapped__(list(filtered))
    with pytest.raises(ValueError):
        assert list(filtered_descriptions)


def test_card_number_generator_1(start: int = 1, stop: int = 10) -> None:
    card_number = gen.card_number_generator.__wrapped__(start, stop)
    """Тестирование функции card_number_generator, первых 10 номеров"""
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
    assert next(card_number) == "0000 0000 0000 0006"


def test_card_number_generator_2(
    start: int = 100000000000, stop: int = 100000000005
) -> None:
    """Тестирование функции card_number_generator, следующих 5 номеров
    после номера 100000000000"""
    card_number = gen.card_number_generator.__wrapped__(start, stop)
    assert next(card_number) == "0000 1000 0000 0000"
    assert next(card_number) == "0000 1000 0000 0001"
    assert next(card_number) == "0000 1000 0000 0002"
    assert next(card_number) == "0000 1000 0000 0003"
    assert next(card_number) == "0000 1000 0000 0004"
    assert next(card_number) == "0000 1000 0000 0005"


def test_card_number_generator_3(start: int = 0, stop: int = 0) -> None:
    """Тестирование функции card_number_generator, нулевой диапазон"""
    card_number = gen.card_number_generator.__wrapped__(start, stop)
    assert next(card_number) == "0000 0000 0000 0000"


def test_card_number_generator_4(start: int = 1, stop: int = 5) -> None:
    """Тестирование функции card_number_generator через список"""
    card_number = gen.card_number_generator.__wrapped__(start, stop)
    assert list(card_number) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


@pytest.mark.parametrize(
    "value, expected",
    [
        (1, "0000 0000 0000 0001"),
        (2, "0000 0000 0000 0002"),
        (3, "0000 0000 0000 0003"),
        (1000, "0000 0000 0000 1000"),
    ],
)
def test_card_number_generator_5(value: int, expected: str) -> None:
    """Тестирование функции card_number_generator через параметризацию"""
    card_number_list = list(gen.card_number_generator.__wrapped__(1, 1005))
    assert card_number_list[value - 1] == expected
