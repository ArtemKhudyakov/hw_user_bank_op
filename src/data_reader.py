import csv
import pathlib as p
from typing import Any, Dict, Hashable, List

import pandas as pd


def csv_reader(
    path_to_csv_file: str = "data/transactions.csv",
) -> list[dict[str, str]]:
    """Функция принимает путь до файла данных формата csv, и возвращает список
    словарей"""
    current_file_path = p.Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent
    file_path = f"{project_root_path}/{path_to_csv_file}"
    try:
        with open(file_path, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            data_list = list(reader)
            return data_list

    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError
    # finally:
    #     return data_list


def xlsx_reader(
    path_to_xlsx_file: str = "data/transactions_excel.xlsx",
) -> List[Dict[Hashable, Any]]:
    """Функция принимает путь до файла данных формата xlsx, и возвращает список
    словарей"""
    current_file_path = p.Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent
    file_path = f"{project_root_path}/{path_to_xlsx_file}"
    try:
        excel_data = pd.read_excel(file_path)
        data_list = excel_data.to_dict(orient="records")
        return data_list
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError
    # finally:
    #     return data_list
