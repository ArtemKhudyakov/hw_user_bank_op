def filter_by_currency(transactions:list[dict[str, str]], currency="USD"):
    if len(transactions) == 0:
        raise ValueError('Список транзакций пуст')
    else:
        filtered_transaction = filter(
            lambda x: x["operationAmount"]["currency"]["code"] == currency,
            transactions,
        )
        # return list(filtered_transaction)
        for transaction in filtered_transaction:
            yield transaction





