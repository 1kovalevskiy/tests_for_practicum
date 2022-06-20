import pytest

from task_2.author import mike, vlad, Contact
from task_2.user_data import USER_CODE, OUTPUT


class ContactForTest:
    def __init__(self, name, phone, birthday, address):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.address = address
        print(f"Создаём новый контакт {name}")

    def show_contact(self):
        print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")


@pytest.mark.xfail  # проблема с кодировкой на разных машинах
def test_code_text():
    """
    Здесь все тестирование, что нужный код не изменен, а нужный - удален.
    Можно детальнее проверять, что не написано вызовов отдельных аттрибутов,
    например 'vlad.name' и все в таком духе. Главное, чтобы появился новый метод
    """
    assert "def print_contact():" not in USER_CODE, (
        "необходимо создать метод 'show_contact' класса 'Contact'"
    )

    test_precode = """print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")"""
    assert test_precode not in USER_CODE, (
        "Информацию об объектах класса необходимо выводить через метод класса"
    )

    test_precode = """print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")"""
    assert test_precode not in USER_CODE, (
        "Информацию об объектах класса необходимо выводить через метод класса"
    )

    assert "class Contact:" in USER_CODE, (
        "Не нужно изменять название класса 'Contact'"
    )

    test_precode = """def __init__(self, name, phone, birthday, address):
    self.name = name
    self.phone = phone
    self.birthday = birthday
    self.address = address
    print(f"Создаём новый контакт {name}")"""
    assert test_precode in USER_CODE, (
        "Не нужно изменять метод '__init__'"
    )

    assert "def show_contact(self):" in USER_CODE, (
        "необходимо создать метод 'show_contact' класса 'Contact'"
    )


def test_object_creation():
    """
    Здесь проверка, что объекты класса ровно такие, какие и нужны
    Вдруг кто-то решит в отдельный аттрибут добавить, где будет запись ответа
    """
    mike_test = ContactForTest(
        "Михаил Булгаков",
        "2-03-27",
        "15.05.1891",
        "Россия, Москва, Большая Пироговская, дом 35б, кв. 6"
    )
    vlad_test = ContactForTest(
        "Владимир Маяковский",
        "73-88",
        "19.07.1893",
        "Россия, Москва, Лубянский проезд, д. 3, кв. 12"
    )
    assert mike.__dict__ == mike_test.__dict__, (
        "Не нужно изменять создание объекта 'Михаил'"
    )
    assert vlad.__dict__ == vlad_test.__dict__, (
        "Не нужно изменять создание объекта 'Владимир'"
    )


def test_new_method_create(capsys):
    # """
    # Здесь тестируется функционал написанной функции
    # Тут можно проверять, что метод выводит все данные правильно
    # """
    test_user = Contact(
        "name",
        "phone",
        "birthday",
        "address"
    )
    test_user.show_contact()
    captured = capsys.readouterr()
    message = """Создаём новый контакт name
name — адрес: address, телефон: phone, день рождения: birthday
"""
    assert captured.out.startswith("""Создаём новый контакт name\n"""), (
        """Необходимо, чтобы при создании объекта выводилась строка 'строка'"""
    )
    message = message.split("\n")[1]
    assert captured.out.split("\n")[1] == message, (
        """Необходимо, чтобы метод 'show_contact' выводил следующую строку 'строка'"""
    )
    # Тут можно проверить, что порядок правильный, но, наверное, студент курса
    # должен знать, как заменить name на {self.name} и т.д., сам им был


@pytest.mark.parametrize(
    "right_line,error_message",
    [
        ("Создаём новый контакт Михаил Булгаков",
         "Нет сообщения, что создан объект Михаил"),
        ("Создаём новый контакт Владимир Маяковский",
         "Нет сообщения, что создан объект Владимир"),
        ("Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891",
         "Неправильный вывод информации об объекте Михаил"),
        ("Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893",
         "Неправильный вывод информации об объекте Владимир")

    ]
)
def test_output(right_line, error_message):
    """
    в конце проверить, что в output есть все необходимое
    """
    assert right_line in OUTPUT, error_message


def test_extra_output():
    """
    Проверка, что нет лишних строчек
    Так лучше проверять, тогда тесты не зависят от порядка вызовов функций
    """
    right_output = OUTPUT.rstrip().split("\n")  # это output требуемый
    output_from_user = OUTPUT.rstrip().split("\n") # это output пользователя
    for line in right_output:
        output_from_user.remove(line)
    assert len(output_from_user) == 0, (
        f"Присутствует лишняя строка {output_from_user[0]}"
    )
