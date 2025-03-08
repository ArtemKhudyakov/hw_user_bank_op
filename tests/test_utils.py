from typing import Any

import src.utils as utils


def test_transactions_data(
    first_transaction_json_data: dict[str, Any],
) -> None:
    transactions_list = utils.transactions_data("data/operations.json")
    if transactions_list:
        assert transactions_list[0] == first_transaction_json_data


def test_transactions_data_empty() -> None:
    transactions_list = utils.transactions_data("empty.json")
    assert transactions_list == []
