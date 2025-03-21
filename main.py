import src.utils as utils
import src.data_reader as data_reader
import src.processing as processing


def main():
    print(
        "\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
    operations_list = []
    start_choice = ''
    filter_choice = ''
    while True:
        start_choice = input("""
        Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Для выхода из программы введите `q`

""")
        if start_choice == '1':
            print("Для обработки выбран JSON-файл.")
            operations_list = utils.transactions_data()
            print(operations_list)
            break

        elif start_choice == '2':
            print("Для обработки выбран CSV-файл.")
            operations_list = data_reader.csv_reader()
            print(operations_list)
            break

        elif start_choice == '3':
            print("Для обработки выбран XLSX-файл.")
            operations_list = data_reader.xlsx_reader()
            print(operations_list)

            break
        elif start_choice == 'q':
            break

        else:
            print("Операция не распознана")

    while True:
        filter_choice = input("""
Программа: Введите статус, по которому 
необходимо выполнить фильтрацию. Доступные фильтры: 
EXECUTED, CANCELED, PENDING
""").upper()
        print(filter_choice)
        print (len(operations_list))
        print(operations_list[1].get('state'))
        if filter_choice == 'EXECUTED' or filter_choice == 'CANCELED' or filter_choice == 'PENDING':
            filtered_operations_list = processing.filter_by_state(operations_list)
            print(filtered_operations_list)


main()
