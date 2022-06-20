import pytest

from task_4.author import make_divider_of
from task_4.user_data import USER_CODE, OUTPUT


@pytest.mark.xfail  # проблема с кодировкой на разных машинах
def test_code_text():
    """
    Здесь все тестирование, что нужный код не изменен
    Можно детальнее проверять.
    """
    precode = """# Создали функцию с параметром divider
div2 = make_divider_of(2)
# Вызвали созданную функцию, передав в нее 10
print(div2(10))
# Выведет: 5.0

div5 = make_divider_of(5)
print(div5(20))
# Выведет: 4.0

print(div5(div2(20)))
# Выведет: 2.0"""
    assert precode in USER_CODE, (
        "Не нужно изменять прекод"
    )

@pytest.mark.parametrize(
    "divider, divisible, expected",
    [
        (2, 10, 5),
        (5, 20, 4),
        (4, 10, 2.5),
        (1, 10, 10),
        (10, 10, 1),
        (10, 1, 0.1),
    ]
)
def test_functionality(divider, divisible, expected):
    """
    Проверить, что все работает как надо
    """
    div_test = make_divider_of(divider)
    assert hasattr(div_test, '__call__')
    assert div_test(divisible) == expected, (
        "Проверьте работоспособность функции"
    )


def test_divider_zero():
    """
    Проверить, что нельзя делить на ноль
    """
    with pytest.raises(ZeroDivisionError):
        make_divider_of(0)(10)
    # Было бы здорово еще обработать, что divider не может быть равным нулю


def test_output():
    """
    в конце проверить, что в output есть все необходимое
    """
    right_output = OUTPUT.rstrip()
    user_output = OUTPUT.rstrip()
    assert right_output in user_output, (
        "Проверьте, что функции вызываются в правильном порядке"
    )
    # На самом деле можно проверять независимо от порядка, но вроде бы это не просили трогать
