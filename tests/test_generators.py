import pytest
import src.generators as gen
from typing import Collection


def test_filter_by_currency_usd(
        list_of_transactions: list[dict[str, Collection]], currency: str = "USD"
) -> None:
    filter_by_currency_usd = gen.filter_by_currency(
        list_of_transactions, currency
    )

    assert next(filter_by_currency_usd) == list_of_transactions[0]
    assert next(filter_by_currency_usd) == list_of_transactions[1]
    assert next(filter_by_currency_usd) == list_of_transactions[3]


def test_filter_by_currency_all(
        list_of_transactions: list[dict[str, Collection]],
        transactions_by_usd: list[dict[str, Collection]],
        currency: str = "USD",
) -> None:
    filter_by_currency_usd = gen.filter_by_currency(
        list_of_transactions, currency
    )
    assert list(filter_by_currency_usd) == transactions_by_usd


def test_filter_by_currency_rub(
        list_of_transactions: list[dict[str, Collection]],
        transactions_by_rub: list[dict[str, Collection]],
        currency: str = "RUB",
) -> None:
    filter_by_currency_rub = gen.filter_by_currency(
        list_of_transactions, currency
    )
    assert list(filter_by_currency_rub) == transactions_by_rub


def test_filter_by_currency_empty(transactions: list = [],
                                  currency: str = "USD") -> None:
    with pytest.raises(ValueError):
        assert list(gen.filter_by_currency(transactions, currency))


def test_filter_by_currency_without_usd(
        transactions_by_rub:list[dict[str, Collection]], currency: str = "USD"
) -> None:
    assert list(gen.filter_by_currency(transactions_by_rub, currency)) == []


def test_filter_by_currency_eur(list_of_transactions: list[dict[str, Collection]],
                                currency: str = "EUR") -> None:
    assert list(gen.filter_by_currency(list_of_transactions, currency)) == []
