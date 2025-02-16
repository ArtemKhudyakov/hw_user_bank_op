import pytest
from mypy.state import state

import src.processing as proc


def test_filter_by_state_ex(parent_test_data, filtered_test_data_executed):
    """Тест функции filter_by_state. Функция должна принимать список операций
    и возвращать список операций отфильтрованный по параметру 'state'. Данные
    по каждой операции представлены в виде словаря
    {"id": "41428829", "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}.
    Фильтрация по состоянию "EXECUTED" """
    assert (proc.filter_by_state(parent_test_data) ==
            filtered_test_data_executed)

def test_filter_by_state_canc(parent_test_data, filtered_test_data_canceled):
    """Тест функции filter_by_state. Функция должна принимать список операций
    и возвращать список операций отфильтрованный по параметру 'state'. Данные
    по каждой операции представлены в виде словаря
    {"id": "41428829", "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364"}.
    Фильтрация по состоянию "CANCELED" """
    assert (proc.filter_by_state(parent_test_data, state = "CANCELED") ==
            filtered_test_data_canceled)


empty_data =[([],'error'),
             ([{"id": "41428829", "state": "",
                "date": "2019-07-03T18:35:29.512364"}],'error'),
             ([{"id": "41428829"}], 'error'), ([{}], 'error')]

@pytest.mark.parametrize("value, expected", empty_data)
def test_filter_by_state_empty(value, expected):
    if len(value) == 0:
        with pytest.raises(ValueError):
            assert proc.filter_by_state(value)
    elif len(value) > 0:
        for operation in value:
            if operation.get(state) == '' or operation.get(state) == None:
                with pytest.raises(ValueError):
                    assert proc.filter_by_state(value)



