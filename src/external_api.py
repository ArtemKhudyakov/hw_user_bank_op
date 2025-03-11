import os
from typing import Any

import requests
from dotenv import load_dotenv


def convert_into_rub(transaction: dict[str, Any]) -> Any:
    """Функция конвертации валюты из USD и EUR в рубли принимает на вход
    словарь с данными о транзакции и возвращает сумму транзакции (ключ amount)
    в рублях, тип данных float. Функция обращается к внешнему сервису
    apilayer.com"""
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
            if status_code == 200:
                result = round(float(response.json()["result"]), 2)
                return result
            else:
                raise Exception
    else:
        raise ValueError("транзакций нет")
