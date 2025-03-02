import tempfile as tmp
import time as t

import pytest

import src.decorators as decorators


def test_dec_log_1():
    """Тест, что декоратор не меняет результат функции"""
    @decorators.log(None)
    def division(x=10, y=2):
        return x / y

    result = division()
    assert result == 5


def test_dec_log_error():
    """Тест, что декоратор выбрасывает ошибку"""
    @decorators.log(None)
    def division(x=10, y=0):
        return x / y

    with pytest.raises(Exception):
        division()


def test_dec_log_capsys(capsys):
    """Тест, что декоратор верно записывает лог"""
    @decorators.log(None)
    def hello_world():
        return "Hello, World!"

    start_time = t.asctime(t.localtime())
    hello_world()
    end_time = t.asctime(t.localtime())
    log = (f"\n"
"        ##########################\n"
"Функция hello_world\n"
f"Время начала выполнения {start_time}\n"
"Функция hello_world успешно выполнена.\n"
"Результат: Hello, World!\n"
f"Время Завершения hello_world {end_time}"
    )

    captured = capsys.readouterr()
    captured_text = captured.out
    assert captured_text.split("\n")[:-3] == log.split("\n")


def test_dec_log_into_file():
    """Тест, что декоратор записывает лог в указанный файл"""
    with tmp.TemporaryDirectory() as tmp_dir:

        @decorators.log(f"{tmp_dir}/test_log_tmp.txt")
        def hello_world():
            return "Hello, World!"

        hello_world()
        with open(f"{tmp_dir}/test_log_tmp.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            assert "Время начала выполнения" in lines[3:4][0]
