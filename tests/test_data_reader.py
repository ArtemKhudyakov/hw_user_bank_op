from typing import Any, Dict, Hashable, List
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.data_reader import csv_reader, xlsx_reader


@patch("pandas.read_excel")
def test_xlsx_reader_success(
    mock_read_excel: Mock, three_transactions: List[Dict[Hashable, Any]]
) -> None:
    """Тест успешного чтения файла"""
    mock_data: pd.DataFrame = pd.DataFrame(three_transactions)
    mock_read_excel.return_value = mock_data
    result: List[Dict[Hashable, Any]] = xlsx_reader()
    assert result[0] == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
    mock_read_excel.assert_called_once()


def test_xlsx_reader_file_not_found() -> None:
    """Тест обработки ошибки, если файл не найден"""
    with pytest.raises(FileNotFoundError):
        data = xlsx_reader("data/transac.xlsx")
        assert data


@patch("pandas.read_excel")
def test_xlsx_reader_empty_file(mock_read_excel: Mock) -> None:
    mock_data: pd.DataFrame = pd.DataFrame()
    mock_read_excel.return_value = mock_data
    result: List[Dict[Hashable, Any]] = xlsx_reader()
    assert result == []


@patch("csv.DictReader")
def test_csv_reader_success(
    mock_DictReader: Mock, three_transactions: List[Dict[str, str]]
) -> None:
    """Тест успешного чтения файла"""
    mock_data = three_transactions
    mock_DictReader.return_value = mock_data
    result: List[Dict[str, str]] = csv_reader()
    assert result[0] == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
    mock_DictReader.assert_called_once()


def test_csv_reader_file_not_found() -> None:
    """Тест обработки ошибки, если файл не найден"""
    with pytest.raises(FileNotFoundError):
        data = csv_reader("data/transac.xlsx")
        assert data


@patch("csv.DictReader")
def test_csv_reader_empty_file(mock_read_csv: Mock) -> None:
    mock_data: List[Dict[str, str]] = []
    mock_read_csv.return_value = mock_data
    result: List[Dict[str, str]] = csv_reader()
    assert result == []
