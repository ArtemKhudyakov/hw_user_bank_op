import src.decorators as decorators
import pytest
import time as t


def test_dec_log_1():
    @decorators.log(None)
    def division(x=10, y=2):
        return x / y

    result = division()
    assert result == 5


def test_dec_log_error():
    @decorators.log(None)
    def division(x=10, y=0):
        return x / y

    with pytest.raises(Exception):
        division()


def test_dec_log_capsys(capsys):
    @decorators.log(None)
    def hello_world():
        return 'Hello, World!'
    start_time = t.asctime(t.localtime())
    start_time_epoch = t.time()
    result = hello_world()
    end_time = t.asctime(t.localtime())
    end_time_epoch = t.time()
    total_time = end_time_epoch - start_time_epoch
    log = (f'\n'
 '            ##########################\n'
 'Функция hello_world\n'
 f'Время начала выполнения {start_time}\n'
 'Функция hello_world успешно выполнена.\n'
 'Результат: Hello, World!\n'
 f'Время Завершения hello_world {end_time}')

    captured = capsys.readouterr()
    captured_text = captured.out
    assert captured_text.split('\n')[:-3] == log.split('\n')

