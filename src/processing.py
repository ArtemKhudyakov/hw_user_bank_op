def filter_by_state(
    operations: list[dict[str, str]], state: str = "EXECUTED"
) -> list[dict[str, str]]:
    """Функция принимает список операций и возвращает список операций
    отфильтрованный по параметру 'state'. Данные по каждой операции
    представлены в виде словаря."""
    filtered_operations: list[dict[str, str]] = [
        operation for operation in operations if operation["state"] == state
    ]
    return filtered_operations


def sort_by_date(
    operations: list[dict[str, str]], descending: bool = True
) -> list[dict[str, str]]:
    """Функция принимает список операций и возвращает отсортированный
    по дате список. По умолчанию сортировка происходит по убыванию,
    т.е. последняя операция выводится первой"""
    sorted_operations: list[dict[str, str]] = sorted(
        operations, key=lambda x: x["date"], reverse=descending
    )
    return sorted_operations
