from typing import Any
from unittest.mock import Mock, patch

import pytest

import src.external_api as external_api


def test_convert_into_rub_1(
    first_transaction_json_data: dict[str, Any],
) -> None:
    """Тест функции convert_into_rub, если транзакция в рублях"""
    assert external_api.convert_into_rub(first_transaction_json_data) == str(
        31957.58
    )


def test_convert_into_rub_2() -> None:
    """Тест функции convert_into_rub, если транзакция пустая"""
    with pytest.raises(ValueError):
        external_api.convert_into_rub({})


@patch("requests.request")
def test_convert_into_rub_3(
    mock_request: Mock, two_transactions_json_data: list[dict[str, Any]]
) -> None:
    """Тест функции convert_into_rub, если внешний ресурс отвечает с ошибкой"""
    transaction = two_transactions_json_data[1]
    mock_response = Mock()
    mock_response.status_code = 500
    mock_request.return_value = mock_response
    with pytest.raises(Exception):
        external_api.convert_into_rub(transaction)
    mock_request.assert_called_once()


@patch("requests.request")
def test_convert_into_rub_4(
    mock_request: Mock, two_transactions_json_data: list[dict[str, Any]]
) -> None:
    """Тест функции convert_into_rub, если транзакция в долларах"""
    transaction = two_transactions_json_data[1]
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 822137.00}
    mock_request.return_value = mock_response
    result = external_api.convert_into_rub(transaction)
    assert result == 822137.00
    mock_request.assert_called_once()
