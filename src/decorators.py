from functools import wraps
import time as t


def log(file_name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time_epoch = t.time()
            start_time = t.asctime(t.localtime())
            end_time_epoch = t.time()
            end_time = t.asctime(t.localtime())
            total_time = end_time_epoch - start_time_epoch
            try:
                result = func(*args, **kwargs)
                log_message = f'''
Функция {func.__name__}
начало выполнения функции: {start_time}
Конец выполнения функции: {end_time}
Затраченное время: {total_time}
Результат выполнения функции: {result}
'''
                return result
            except Exception as e:
                error_type = type(e).__name__
                log_message = f'''
Функция {func.__name__} выполнена с ОШИБКОЙ!
Ошибка: {error_type}
Inputs: {args}, {kwargs}
'''
                raise
            finally:
                if file_name:
                    with open(file_name, 'a', encoding='utf-8') as file:
                        file.write(log_message)
                else: print(log_message)
        return wrapper
    return decorator
