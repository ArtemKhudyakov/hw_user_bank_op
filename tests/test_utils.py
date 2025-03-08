from typing import Any

import src.utils as utils


def test_transactions_data(
    first_transaction_json_data: dict[str, Any],
) -> None:
    """Тест функции test_transactions_data, если в функцию передаются верные
    значения"""
    transactions_list = utils.transactions_data("data/operations.json")
    if transactions_list:
        assert transactions_list[0] == first_transaction_json_data


def test_transactions_data_empty() -> None:
    """Тест функции test_transactions_data, если в функцию передается неверный
    путь к файлу"""
    transactions_list = utils.transactions_data("empty.json")
    assert transactions_list == []
