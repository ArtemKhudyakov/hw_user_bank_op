import re
from collections import Counter
from typing import Any, Dict, List


def op_searching_by_description(
    string_for_searching: str, operations_list: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """Принимает список словарей с данными о банковских операциях и строку
    поиска, а возвращать список словарей, у которых в описании есть данная
    строка."""
    operations_by_description = [
        operation
        for operation in operations_list
        if re.search(
            string_for_searching, operation["description"], re.IGNORECASE
        )
    ]
    return operations_by_description


def op_counter_by_category(
    operations_list: List[Dict[str, Any]], srch_categories_list: List[str]
) -> Dict[str, Any]:
    """Функция принимает список словарей с данными о банковских операциях и
    список категорий операций, возвращать словарь, в котором ключи — это
    названия категорий, а значения — это количество операций в каждой
    категории."""
    srch_counter: Dict[str, Any] = {}
    op_category_list: List[str] = [
        str(operation["description"]).capitalize()
        for operation in operations_list
    ]
    category_counter: Counter[str] = Counter(op_category_list)

    for i in srch_categories_list:
        if str(i.capitalize()) in list(category_counter.keys()):
            srch_counter[i.capitalize()] = category_counter[i.capitalize()]
        else:
            srch_counter[i] = 0

    return srch_counter
