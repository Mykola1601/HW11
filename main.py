
# HW 10

from collections import UserDict
from datetime import date, timedelta, datetime
import re 


def normalize_phone(phone):
    numbers = re.findall('\d+', str(phone))
    phone = (''.join(numbers))
    if len(phone) == 10 :
        return phone
    else:
        return None


# поля
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value
  

class Birthday(Field):
    def __init__(self, value):
        self.value = value
  

class Phone(Field):
    def __init__(self, value):
        if not normalize_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(None)

    def add_phone(self, *args):
        self.phones.append(args[0])
        # name = self.name.value

    def remove_phone(self, *args):
        phone = args[0]
        self.phones.remove(phone)

    def edit_phone(self, *args):
        phone = args[0]
        new_phone = args[1]
        self.phones.append(new_phone)
        self.phones.remove(phone)
        
    def find_phone(self, *args):
        phone = args[0]
        if phone in self.phones:
            return Phone(phone)
        return None

    def days_to_birthday(self):
        current_date = date.today()
        birth_date = datetime.strptime(str(self.birthday.value), '%d-%m-%Y')
        birth_date = datetime(year=current_date.year, month=birth_date.month,day=birth_date.day).date() 
        delta = birth_date - current_date
        if delta.days >0:
            print(f"{delta.days} days to birthday ")
        else:
            birth_date = datetime(year=current_date.year+1, month=birth_date.month,day=birth_date.day).date() 
            delta = birth_date - current_date
            print(f"{delta.days} days to birthday ")

    def add_birthday(self, *args):
        self.birthday = Birthday(args[0]) 
        # name = self.name.value


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(self.phones)}{'; Birthday '+ self.birthday.value if self.birthday.value else '' }"


class AddressBook(UserDict):
    def add_record(self, *args): 
        name = args[0].name.value
        self.data[name] = args[0]

    def find(self, *args):
        name = args[0]
        if name in self.data:
            return  self.data[name]
        else:
            return None

    def delete(self, *args):
        if self.data.get(args[0]):
            self.data.pop(args[0])


# book = AddressBook()


def main():
    book = AddressBook()


# ========================================
if __name__ == "__main__":
    main()




    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # add birthday
    john_record.add_birthday("19-10-2011")
    john_record.days_to_birthday()


    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555


    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # add birthday
    # jane_record.add_birthday("11.11.2011")




