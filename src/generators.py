from typing import Iterator
from typing import Collection
from typing import Callable


# from typing import TypeGuard
# from typing import Any


def filter_by_currency(transactions: list[dict[str, Collection[str]]],
                       currency: str = "USD") -> Iterator[
    dict[str, Collection]]:
    if len(transactions) == 0:
        raise ValueError("Список транзакций пуст")
    else:
        filtered_transaction: Callable[[dict[str, Collection]]] = filter(
            lambda x: x["operationAmount"]["currency"]["code"] == currency,
            transactions)
        for transaction in filtered_transaction:
            yield transaction
