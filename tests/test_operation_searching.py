import unittest
from typing import Any, Dict, List

from src.operation_searching import (
    op_counter_by_category,
    op_searching_by_description
)


class TestOpCounterByCategory(unittest.TestCase):
    def test_basic_functionality(self) -> None:
        """Тест на базовую функциональность."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries", "amount": 50},
            {"description": "Transport", "amount": 20},
            {"description": "Groceries", "amount": 30},
            {"description": "Entertainment", "amount": 100},
        ]
        categories_list: List[str] = [
            "Groceries",
            "Transport",
            "Entertainment",
        ]
        expected_result: Dict[str, int] = {
            "Groceries": 2,
            "Transport": 1,
            "Entertainment": 1,
        }
        result = op_counter_by_category(operations_list, categories_list)
        self.assertEqual(result, expected_result)

    def test_empty_operations_list(self) -> None:
        """Тест на пустой список операций."""
        operations_list: List[Dict[str, Any]] = []
        categories_list: List[str] = ["Groceries", "Transport"]
        expected_result: Dict[str, int] = {"Groceries": 0, "Transport": 0}
        result = op_counter_by_category(operations_list, categories_list)
        self.assertEqual(result, expected_result)

    def test_empty_categories_list(self) -> None:
        """Тест на пустой список категорий."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries", "amount": 50},
            {"description": "Transport", "amount": 20},
        ]
        categories_list: List[str] = []
        expected_result: Dict[str, int] = {}
        result = op_counter_by_category(operations_list, categories_list)
        self.assertEqual(result, expected_result)

    def test_category_not_found(self) -> None:
        """Тест на случай, когда категория отсутствует в операциях."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries", "amount": 50},
            {"description": "Transport", "amount": 20},
        ]
        categories_list: List[str] = ["Groceries", "Health"]
        expected_result: Dict[str, int] = {"Groceries": 1, "Health": 0}
        result = op_counter_by_category(operations_list, categories_list)
        self.assertEqual(result, expected_result)

    def test_case_insensitivity(self) -> None:
        """Тест на регистронезависимость."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "groceries", "amount": 50},
            {"description": "TRANSPORT", "amount": 20},
            {"description": "Groceries", "amount": 30},
        ]
        categories_list: List[str] = ["Groceries", "Transport"]
        expected_result: Dict[str, int] = {"Groceries": 2, "Transport": 1}
        result = op_counter_by_category(operations_list, categories_list)
        self.assertEqual(result, expected_result)

    def test_duplicate_categories(self) -> None:
        """Тест на дублирование категорий в списке."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries", "amount": 50},
            {"description": "Transport", "amount": 20},
        ]
        categories_list: List[str] = ["Groceries", "Groceries", "Transport"]
        expected_result: Dict[str, int] = {"Groceries": 1, "Transport": 1}
        result = op_counter_by_category(operations_list, categories_list)
        self.assertEqual(result, expected_result)


class TestOpSearchingByDescription(unittest.TestCase):
    def test_basic_functionality(self) -> None:
        """Тест на базовую функциональность."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "Transport via Uber", "amount": 20},
            {"description": "Groceries at Aldi", "amount": 30},
            {"description": "Entertainment: Cinema", "amount": 100},
        ]
        string_for_searching: str = "Groceries"
        expected_result: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "Groceries at Aldi", "amount": 30},
        ]
        result = op_searching_by_description(
            string_for_searching, operations_list
        )
        self.assertEqual(result, expected_result)

    def test_case_insensitivity(self) -> None:
        """Тест на регистронезависимость."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "Transport via Uber", "amount": 20},
            {"description": "groceries at Aldi", "amount": 30},
            {"description": "Entertainment: Cinema", "amount": 100},
        ]
        string_for_searching: str = "groceries"
        expected_result: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "groceries at Aldi", "amount": 30},
        ]
        result = op_searching_by_description(
            string_for_searching, operations_list
        )
        self.assertEqual(result, expected_result)

    def test_no_matches(self) -> None:
        """Тест на случай, когда совпадений нет."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "Transport via Uber", "amount": 20},
            {"description": "Entertainment: Cinema", "amount": 100},
        ]
        string_for_searching: str = "Restaurant"
        expected_result: List[Dict[str, Any]] = []
        result = op_searching_by_description(
            string_for_searching, operations_list
        )
        self.assertEqual(result, expected_result)

    def test_empty_operations_list(self) -> None:
        """Тест на пустой список операций."""
        operations_list: List[Dict[str, Any]] = []
        string_for_searching: str = "Groceries"
        expected_result: List[Dict[str, Any]] = []
        result = op_searching_by_description(
            string_for_searching, operations_list
        )
        self.assertEqual(result, expected_result)

    def test_empty_search_string(self) -> None:
        """Тест на пустую строку поиска."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "Transport via Uber", "amount": 20},
            {"description": "Entertainment: Cinema", "amount": 100},
        ]
        string_for_searching: str = ""
        expected_result: List[Dict[str, Any]] = operations_list
        result = op_searching_by_description(
            string_for_searching, operations_list
        )
        self.assertEqual(result, expected_result)

    def test_partial_match(self) -> None:
        """Тест на частичное совпадение."""
        operations_list: List[Dict[str, Any]] = [
            {"description": "Groceries at Walmart", "amount": 50},
            {"description": "Transport via Uber", "amount": 20},
            {"description": "Entertainment: Cinema", "amount": 100},
        ]
        string_for_searching: str = "via"
        expected_result: List[Dict[str, Any]] = [
            {"description": "Transport via Uber", "amount": 20},
        ]
        result = op_searching_by_description(
            string_for_searching, operations_list
        )
        self.assertEqual(result, expected_result)
