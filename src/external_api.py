import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_into_rub(transaction: dict[str, Any]) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список
    словарей с данными о финансовых транзакциях. Если файл пустой, содержит
    не список или не найден, функция возвращает пустой список."""
    if transaction:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            result = transaction["operationAmount"]["amount"]
            return result

        else:
            load_dotenv(dotenv_path=".env")
            API_KEY = os.getenv("API_KEY_FOR_APILAYER")
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?to="
                f"RUB&from="
                f"{transaction["operationAmount"]["currency"]["code"]}"
                f"&amount={transaction["operationAmount"]["amount"]}"
            )

            payload: dict = {}
            headers = {"apikey": API_KEY}

            response = requests.request(
                "GET", url, headers=headers, data=payload
            )
            status_code = response.status_code
            result = round(float(response.json()["result"]), 2)
            if status_code == 200:
                return result
            else:
                raise Exception
    else:
        raise ValueError("транзакций нет")
