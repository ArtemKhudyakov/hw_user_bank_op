import src.utils as utils
import src.data_reader as data_reader


def main():
    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")

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

            break

        elif start_choice == '2':
            print("Для обработки выбран CSV-файл.")

            break
        elif start_choice == '3':
            print("Для обработки выбран XLSX-файл.")

            break
        elif start_choice == 'q':
            break

        else:
            print("Операция не распознана")


main()