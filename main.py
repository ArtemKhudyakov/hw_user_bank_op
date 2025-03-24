import src.data_reader as data_reader
import src.generators as gen
import src.operation_searching as op_search
import src.processing as processing
import src.utils as utils
import src.widjet as widjet


def main() -> None:
    print(
        "\nПривет! Добро пожаловать в программу работы с "
        "банковскими транзакциями."
    )
    operations_list: list | None = []
    filtered_operations_list: list = []
    sorted_filtered_op: list = []
    sorted_by_currency: list = []
    while True:
        start_choice = input(
            """
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Для выхода из программы введите `q`
"""
        )
        if start_choice == "q":
            exit()

        elif start_choice not in ["1", "2", "3"]:
            print("Операция не распознана")
            continue

        else:
            if start_choice == "1":
                print("Для обработки выбран JSON-файл.")
                operations_list = utils.transactions_data()

            elif start_choice == "2":

                print("Для обработки выбран CSV-файл.")
                operations_list = data_reader.csv_reader()

            elif start_choice == "3":
                print("Для обработки выбран XLSX-файл.")
                operations_list = data_reader.xlsx_reader()

        while True:
            filter_choice = input(
                """
Программа: Введите статус, по которому
необходимо выполнить фильтрацию. Доступные фильтры:
EXECUTED, CANCELED, PENDING
"""
            ).upper()
            if filter_choice not in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f'Статус операции "{filter_choice}" недоступен')
                action = input(
                    """
Для повторного ввода статуса операции нажмите "Enter"
Для возврата в предыдущее меню введите "b"
Для выхода из программы введите "q"
"""
                ).lower()
                if action == "q":
                    exit()
                elif action == "b":
                    break
                else:
                    continue
            else:
                filtered_operations_list = list(
                    processing.filter_by_state(operations_list, filter_choice)
                )
                sort_choice = input(
                    """
Отсортировать операции по дате? Y/N
"""
                ).capitalize()

                if sort_choice == "Y":
                    print("\nВыбрана сортировка по дате\n")
                    print("Отсортировать по возрастанию или по убыванию?")
                    upscending_descending_choice = input(
                        """
Для сортировки по возрастанию введите 1
Для сортировки по убыванию нажмите "Enter"
"""
                    )
                    if upscending_descending_choice == "1":
                        sorted_filtered_op = processing.sort_by_date(
                            filtered_operations_list, False
                        )
                    else:
                        sorted_filtered_op = processing.sort_by_date(
                            filtered_operations_list
                        )
                else:
                    print("\nБез сортировки по дате\n")
                    sorted_filtered_op = filtered_operations_list

            currency_filter = input(
                """
Отфильтровать транзакции по валюте? Y/N
"""
            ).upper()
            while True:
                if currency_filter != "Y":
                    sorted_by_currency = sorted_filtered_op
                else:
                    currency_code_choice = input(
                        """
Выберите валюту для фильтрации RUB, EUR, USD, CNY и т.д.
"""
                    ).upper()
                    if len(currency_code_choice) != 3:
                        action = input(
                            """Введен не корректный код валюты
Для повторного ввода кода валюты нажмите "Enter"
Для отмены фильтрации по валюте "b"
Для выхода из программы введите "q"
"""
                        ).lower()
                        if action == "q":
                            exit()
                        elif action == "b":
                            sorted_by_currency = sorted_filtered_op
                        else:
                            continue
                    else:
                        sorted_by_currency = list(
                            gen.filter_by_currency(
                                sorted_filtered_op, currency_code_choice
                            )
                        )

                filter_by_word_choice = input(
                    """
Отфильтровать список транзакций по определенному слову в описании? Y/N
"""
                ).upper()
                if filter_by_word_choice == "Y":
                    string_for_searching = input(
                        """
Введите текст для фильтрации по типу операции
"""
                    )
                    filtered_by_word = op_search.op_searching_by_description(
                        string_for_searching, sorted_by_currency
                    )
                else:
                    filtered_by_word = sorted_by_currency
                print("\nРаспечатываю итоговый список транзакций...")
                if len(filtered_by_word) == 0:
                    print(
                        "\nНе найдено ни одной транзакции, "
                        "подходящей под ваши условия фильтрации"
                    )
                else:
                    print(
                        f"\nВсего банковских операций в выборке: "
                        f"{len(filtered_by_word)}"
                    )
                    for operation in filtered_by_word:
                        print(
                            f"\n{widjet.get_date(operation["date"])} "
                            f"{operation["description"]}"
                        )
                        if start_choice == "1":
                            amount = operation["operationAmount"]["amount"]
                            currency = operation["operationAmount"][
                                "currency"
                            ]["code"]
                            if operation.get("from"):
                                from_card_numb = widjet.mask_account_card(
                                    operation["from"]
                                )
                                to_card_numb = widjet.mask_account_card(
                                    operation["to"]
                                )
                                print(
                                    f"{from_card_numb} " f"--> {to_card_numb} "
                                )
                            else:
                                to_card_numb = widjet.mask_account_card(
                                    operation["to"]
                                )
                                print(f"{to_card_numb} ")
                            print(f"Сумма:{amount}" f" {currency}")
                        else:
                            amount = operation["amount"]
                            currency = operation["currency_code"]
                            if (
                                str(operation["from"]) == "nan"
                                or operation["from"] == ""
                            ):
                                to_card_numb = widjet.mask_account_card(
                                    operation["to"]
                                )
                                print(f"{to_card_numb} ")
                            else:
                                from_card_numb = widjet.mask_account_card(
                                    operation["from"]
                                )
                                to_card_numb = widjet.mask_account_card(
                                    operation["to"]
                                )
                                print(
                                    f"{from_card_numb} " f"--> {to_card_numb} "
                                )
                            print(f"Сумма: {amount} " f"{currency}")
                continue_or_not = input(
                    """
Для выхода из программы введите "q"
Для распечатки новой выборки нажмите "Enter")
"""
                )
                if continue_or_not == "q":
                    exit()
                else:
                    break
            break

if __name__ == "__main__":
    main()

