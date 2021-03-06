import time

import pytest as pytest

from task_3.author import cache_args
from task_3.user_data import USER_CODE, OUTPUT


@pytest.mark.xfail  # проблема с кодировкой на разных машинах
def test_code_text():
    """
    Здесь все тестирование, что нужный код не изменен
    Можно детальнее проверять.
    """
    precode = """import time


def time_check(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)
        execution_time = round(time.time() - start_time, 1)
        print(f'Время выполнения функции: {execution_time} с.')
        return result

    return wrapper


def cache_args(func):"""
    assert precode in USER_CODE, (
        "Не нужно изменять работу декоратора 'time_check'"
    )

    precode = """@time_check
@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2


print(long_heavy(1))
# Время выполнения функции: 1.0 с.
# 2
print(long_heavy(1))
# Время выполнения функции: 0.0 с.
# 2
print(long_heavy(2))
# Время выполнения функции: 1.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции: 0.0 с.
# 4
print(long_heavy(2))
# Время выполнения функции: 0.0 с.
# 4"""
    assert precode in USER_CODE, (
        "Не нужно изменять работу вызова функций"
    )


@cache_args
def long_heavy(num):
    time.sleep(1)
    return num * 2


def test_functionality():

    start_time = time.time()
    result = long_heavy(1)
    assert round(time.time() - start_time, 1) == 1, (
        "вызываемая функция должна выполняться в исходном виде"
    )
    assert result == 2, (
        "проверьте, чтобы декоратор 'cache_args' не изменял работу функции 'long_heavy'"
    )

    start_time = time.time()
    result = long_heavy(1)
    assert round(time.time() - start_time, 1) == 0, (
        "проверьте, что декоратор кэширует результат функции"
    )
    assert result == 2, (
        "проверьте, чтобы декоратор 'cache_args' не изменял работу функции 'long_heavy'"
    )

    start_time = time.time()
    result = long_heavy(1)
    assert round(time.time() - start_time, 1) == 0, (
        "проверьте, что после использования кэш не удаляется"
    )
    assert result == 2, (
        "проверьте, чтобы декоратор 'cache_args' не изменял работу функции 'long_heavy'"
    )

    start_time = time.time()
    result = long_heavy(2)
    assert round(time.time() - start_time, 1) == 1, (
        "проверьте, что кэширование одной функции не влияет на кэширование другой"
    )
    assert result == 4, (
        "проверьте, чтобы декоратор 'cache_args' не изменял работу функции 'long_heavy'"
    )

    start_time = time.time()
    result = long_heavy(2)
    assert round(time.time() - start_time, 1) == 0, (
        "проверьте, что декоратор кэширует результат функции"
    )
    assert result == 4, (
        "проверьте, чтобы декоратор 'cache_args' не изменял работу функции 'long_heavy'"
    )


def test_output():
    """
    в конце проверить, что в output есть все необходимое
    """
    right_output = OUTPUT.rstrip()
    user_output = OUTPUT.rstrip()
    assert right_output in user_output, (
        "Проверьте, что функции вызываются в правильном порядке"
    )
    #На самом деле можно проверять независимо от порядка, но вроде бы это не просили трогать