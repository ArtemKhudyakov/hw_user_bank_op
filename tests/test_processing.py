import pytest
from mypy.state import state

import src.processing as proc


def test_filter_by_state_ex(
    parent_test_data: list[dict[str, str]],
    filtered_test_data_executed: list[dict[str, str]],
) -> None:
    """Тест функции filter_by_state. Функция должна принимать список операций
    и возвращать список операций отфильтрованный по параметру 'state'. Данные
    по каждой операции представлены в виде словаря
    {"id": "41428829", "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}.
    Фильтрация по состоянию "EXECUTED" """
    assert (
        proc.filter_by_state(parent_test_data) == filtered_test_data_executed
    )


def test_filter_by_state_canc(
    parent_test_data: list[dict[str, str]],
    filtered_test_data_canceled: list[dict[str, str]],
) -> None:
    """Тест функции filter_by_state. Функция должна принимать список операций
    и возвращать список операций отфильтрованный по параметру 'state'. Данные
    по каждой операции представлены в виде словаря
    {"id": "41428829", "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}.
    Фильтрация по состоянию "CANCELED" """
    assert (
        proc.filter_by_state(parent_test_data, state="CANCELED")
        == filtered_test_data_canceled
    )


error_data = [
    ([], "error"),
    (
        [
            {
                "id": "41428829",
                "state": "",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "error",
    ),
    ([{"id": "41428829"}], "error"),
    ([{}], "error"),
]


@pytest.mark.parametrize("value, expected", error_data)
def test_filter_by_state_empty(value: list, expected: None) -> None:
    """Тест функции filter_by_state. Функция должна принимать список операций
    и возвращать список операций отфильтрованный по параметру 'state'.
    Данные по каждой операции представлены в виде словаря
    {"id": "41428829", "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}.
    Отработка ошибочного заполнения списка операций"""
    if len(value) == 0:
        with pytest.raises(ValueError):
            assert proc.filter_by_state(value)
    elif len(value) > 0:
        for operation in value:
            if operation.get(state) == "" or operation.get(state) is None:
                with pytest.raises(ValueError):
                    assert proc.filter_by_state(value)


def test_sort_by_date_desc(
    parent_test_data: list[dict[str, str]],
    sorted_by_date_data_descending: list[dict[str, str]],
) -> None:
    """Тест функции sort_by_date. Функция должна принимать список операций
    и возвращать отсортированный по дате список. По умолчанию сортировка
    происходит по убыванию, т.е. последняя операция выводится первой.
    Тестирование убывающей сортировки"""
    assert (
        proc.sort_by_date(parent_test_data) == sorted_by_date_data_descending
    )


def test_sort_by_date_asc(
    parent_test_data: list[dict[str, str]],
    sorted_by_date_data_ascending: list[dict[str, str]],
) -> None:
    """Тест функции sort_by_date. Функция должна принимать список операций
    и возвращать отсортированный по дате список. По умолчанию сортировка
    происходит по убыванию, т.е. последняя операция выводится первой.
    Тестирование восходящей сортировки"""
    assert (
        proc.sort_by_date(parent_test_data, False)
        == sorted_by_date_data_ascending
    )
