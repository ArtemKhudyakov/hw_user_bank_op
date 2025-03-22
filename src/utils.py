import json
import logging
from pathlib import Path
from typing import Any, List, Optional

current_file_path = Path(__file__).resolve()
project_root_path = current_file_path.parent.parent

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(
    f"{project_root_path}/logs/utils.log", encoding="utf-8", mode="w"
)
file_formater = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def transactions_data(
    path_to_json_file: str = "data/operations.json",
) -> Optional[List[Any]]:
    """Функция принимает на вход относительный путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список."""
    json_data: Optional[List[Any]] | None = None
    current_file_path = Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent
    file_path = f"{project_root_path}/{path_to_json_file}"
    try:
        logger.debug(f'Загружаем данные из файла "{path_to_json_file}"')
        with open(file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        json_data = []
    finally:
        logger.debug(f"Возвращаем результат --> {json_data}")
        return json_data
