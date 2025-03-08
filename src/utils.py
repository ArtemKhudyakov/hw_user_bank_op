import json
from pathlib import Path
from typing import Any, List, Optional


def transactions_data(
    path_to_json_file:str = "data/operations.json",
) -> Optional[List[Any]]:
    """Функция принимает на вход относительный путь до JSON-файла и возвращает
список словарей с данными о финансовых транзакциях. Если файл пустой, содержит
не список или не найден, функция возвращает пустой список."""
    json_data: Optional[List[Any]] = None
    current_file_path = Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent
    file_path = f"{project_root_path}/{path_to_json_file}"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
    except Exception:
        json_data = []
    finally:
        return json_data
