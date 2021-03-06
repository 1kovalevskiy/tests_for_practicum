USER_CODE = """
class Contact:
def __init__(self, name, phone, birthday, address):
    self.name = name
    self.phone = phone
    self.birthday = birthday
    self.address = address
    print(f"Создаём новый контакт {name}")

# здесь напишите метод show_contact()
# он будет очень похож на функцию print_contact()
def show_contact(self):
    print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")


mike = Contact(
    "Михаил Булгаков",
    "2-03-27",
    "15.05.1891",
    "Россия, Москва, Большая Пироговская, дом 35б, кв. 6"
)
vlad = Contact(
    "Владимир Маяковский",
    "73-88",
    "19.07.1893",
    "Россия, Москва, Лубянский проезд, д. 3, кв. 12"
)

mike.show_contact()
vlad.show_contact()
"""
OUTPUT = """Создаём новый контакт Михаил Булгаков
Создаём новый контакт Владимир Маяковский
Михаил Булгаков — адрес: Россия, Москва, Большая Пироговская, дом 35б, кв. 6, телефон: 2-03-27, день рождения: 15.05.1891
Владимир Маяковский — адрес: Россия, Москва, Лубянский проезд, д. 3, кв. 12, телефон: 73-88, день рождения: 19.07.1893"""
