import src.generators as gen
import pytest

def test_filter_by_currency_usd(list_of_transactions: list[dict[str, str]],
                                currency: str = 'USD') -> None:
    filter_by_currency_usd = (
        gen.filter_by_currency(list_of_transactions, currency))

    assert next(filter_by_currency_usd) == list_of_transactions[0]
    assert next(filter_by_currency_usd) == list_of_transactions[1]
    assert next(filter_by_currency_usd) == list_of_transactions[3]


def test_filter_by_currency_all(list_of_transactions: list[dict[str, str]],
                                transactions_by_usd: list[dict[str, str]],
                                currency: str = 'USD') -> None:
    filter_by_currency_usd = (
        gen.filter_by_currency(list_of_transactions, currency))
    assert list(filter_by_currency_usd) == transactions_by_usd


def test_filter_by_currency_rub(list_of_transactions: list[dict[str, str]],
                                transactions_by_rub: list[dict[str, str]],
                                currency: str = 'RUB') -> None:
    filter_by_currency_rub = (
        gen.filter_by_currency(list_of_transactions, currency))
    assert list(filter_by_currency_rub) == transactions_by_rub

def test_filter_by_currency_empty(transactions=[],currency: str = 'USD'):
    with pytest.raises(ValueError):
        assert list(gen.filter_by_currency(transactions, currency))

def test_filter_by_currency_without_usd(transactions_by_rub, currency: str = 'USD'):
    assert list(gen.filter_by_currency(transactions_by_rub, currency)) == []

def test_filter_by_currency_eur(list_of_transactions, currency: str = 'EUR'):
    assert list(gen.filter_by_currency(list_of_transactions, currency)) == []
