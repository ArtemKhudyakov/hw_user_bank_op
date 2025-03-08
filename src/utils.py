import json
from pathlib import Path
from typing import Any


def transactions_data(
    file_name: str = "operations.json",
) -> list[dict[str, Any]]:
    json_data = None
    current_file_path = Path(__file__).resolve()
    project_root_path = current_file_path.parent.parent
    file_path = f"{project_root_path}/data/{file_name}"
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json_data = json.load(f)
    except Exception:
        json_data = []
    finally:
        return json_data


# tansac = transactions_data()
# print(tansac)
# for transaction in tansac:
#
#     print(transaction)
#     print()
