import time as t
from functools import wraps
from typing import Any, Callable, Optional, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def log(file_name: Optional[str] = None) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_message = []
            execution_message = []
            start_time_epoch = t.time()
            start_time = t.asctime(t.localtime())
            start_message.append(
                f"""
            ##########################
Функция {func.__name__}
Время начала выполнения {start_time}\n"""
            )
            try:
                result = func(*args, **kwargs)
                if (
                    type(result) is str
                    or type(result) is int
                    or type(result) is float
                    or type(result) is list
                    or type(result) is tuple
                    or type(result) is dict
                ):
                    execution_message.append(
                        f"Функция {func.__name__} "
                        f"успешно выполнена.\n"
                        f"Результат: {result}\n"
                    )
                else:
                    result_list = [
                        x
                        for i, x in enumerate(func(*args, **kwargs))
                        if i < 10
                    ]
                    if len(result_list) == 10:
                        result_list.append("и т.д.")
                    execution_message.append(
                        f"Функция {func.__name__} "
                        f"успешно выполнена.\n"
                        f"Результат: {result_list}\n"
                    )
                return result
            except Exception as e:
                error_type = type(e).__name__
                execution_message.append(
                    f"ОШИБКА!!!\nОшибка: {error_type}\n"
                    f"Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                end_time_epoch = t.time()
                end_time = t.asctime(t.localtime())
                total_time = end_time_epoch - start_time_epoch
                end_log_message = [
                    f"Время Завершения {func.__name__} "
                    f"{end_time}\n"
                    f"Время выполнения {total_time}\n"
                ]
                final_log_message = "".join(
                    start_message + execution_message + end_log_message
                )
                if file_name:
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(final_log_message)
                else:
                    print(final_log_message)

        return wrapper

    return decorator
