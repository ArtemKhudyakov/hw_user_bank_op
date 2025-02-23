from typing import Collection

import pytest

import src.generators as gen


def test_filter_by_currency_usd(
    list_of_transactions: list[dict[str, Collection[str]]],
    currency: str = "USD",
) -> None:
    filter_by_currency_usd = gen.filter_by_currency(
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
    filter_by_currency_usd = gen.filter_by_currency(
        list_of_transactions, currency
    )
    assert list(filter_by_currency_usd) == transactions_by_usd


def test_filter_by_currency_rub(
    list_of_transactions: list[dict[str, Collection[str]]],
    transactions_by_rub: list[dict[str, Collection[str]]],
    currency: str = "RUB",
) -> None:
    filter_by_currency_rub = gen.filter_by_currency(
        list_of_transactions, currency
    )
    assert list(filter_by_currency_rub) == transactions_by_rub


def test_filter_by_currency_empty(
    transactions: list = [], currency: str = "USD"
) -> None:
    with pytest.raises(ValueError):
        assert list(gen.filter_by_currency(transactions, currency))


def test_filter_by_currency_without_usd(
    transactions_by_rub: list[dict[str, Collection[str]]],
    currency: str = "USD",
) -> None:
    assert list(gen.filter_by_currency(transactions_by_rub, currency)) == []


def test_filter_by_currency_eur(
    list_of_transactions: list[dict[str, Collection[str]]],
    currency: str = "EUR",
) -> None:
    assert list(gen.filter_by_currency(list_of_transactions, currency)) == []


def test_transaction_descriptions(
    list_of_transactions: list[dict[str, Collection[str]]],
) -> None:
    description = gen.transaction_descriptions(list_of_transactions)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


def test_transaction_descriptions_empty(transactions: list = []) -> None:
    with pytest.raises(ValueError):
        assert next(gen.transaction_descriptions(transactions)) == ""


def test_transaction_descriptions_with_filter_rub(
    list_of_transactions: list[dict[str, Collection[str]]],
) -> None:
    filtered = gen.filter_by_currency(list_of_transactions, "RUB")
    filtered_descriptions = gen.transaction_descriptions(list(filtered))
    assert list(filtered_descriptions) == [
        "Перевод со счета на счет",
        "Перевод организации",
    ]


def test_transaction_descriptions_with_filter_eur(
    list_of_transactions: list[dict[str, Collection[str]]],
) -> None:
    filtered = gen.filter_by_currency(list_of_transactions, "EUR")
    filtered_descriptions = gen.transaction_descriptions(list(filtered))
    with pytest.raises(ValueError):
        assert list(filtered_descriptions)


def test_card_number_generator_1(start: int = 1, stop: int = 10) -> None:
    card_number = gen.card_number_generator(start, stop)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
    assert next(card_number) == "0000 0000 0000 0006"


def test_card_number_generator_2(
    start: int = 100000000000, stop: int = 100000000005
) -> None:
    card_number = gen.card_number_generator(start, stop)
    assert next(card_number) == "0000 1000 0000 0000"
    assert next(card_number) == "0000 1000 0000 0001"
    assert next(card_number) == "0000 1000 0000 0002"
    assert next(card_number) == "0000 1000 0000 0003"
    assert next(card_number) == "0000 1000 0000 0004"
    assert next(card_number) == "0000 1000 0000 0005"


def test_card_number_generator_3(start: int = 0, stop: int = 0) -> None:
    card_number = gen.card_number_generator(start, stop)
    assert next(card_number) == "0000 0000 0000 0000"


def test_card_number_generator_4(start: int = 1, stop: int = 5) -> None:
    card_number = gen.card_number_generator(start, stop)
    assert list(card_number) == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
