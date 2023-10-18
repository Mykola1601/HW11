
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
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.__birthday = Birthday(None)

    @property
    def ph(self):
        return self.phones

    @ph.setter
    def add_phone(self, phone: str) -> None:
        if not normalize_phone(phone):
            print (f"('{phone}') -> Invalid phone number format != 10digit")
        phone = normalize_phone(phone)
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone_number: str) -> None | str:
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break
        else:
            raise ValueError(f'phone {phone_number} not found ')

    def edit_phone(self, *args):
        old_phone = args[0]
        new_phone = args[1]
        for id, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[id] = Phone(new_phone)
                break
        else:
            raise ValueError(f'phone {phone} not found in the record')        
        
    def find_phone(self, *args):
        phone = args[0]
        if phone in self.phones:
            return Phone(phone)
        return None

    def days_to_birthday(self) :
        if self.__birthday.value:
            current_date = date.today()
            birth_date = self.__birthday.value
            birth_date = datetime(year=current_date.year, month=birth_date.month,day=birth_date.day).date() 
            delta = birth_date - current_date
            if delta.days >=0:
                print(f"{delta.days} days to birthday")
            else:
                birth_date = datetime(year=current_date.year+1, month=birth_date.month,day=birth_date.day).date() 
                delta = birth_date - current_date
                print(f"{delta.days} days to birthday")
        else:
            print('No birthday date')


    @property
    def birthday(self):
        return f'{self.name.value} birthday {self.__birthday.value}'

    @birthday.setter
    def add_birthday(self, *args):
        try:
            birthday = datetime.strptime(str(args[0]), '%Y-%m-%d')
            self.__birthday = Birthday(birthday.date()) 
        except ValueError:
            print('Error input - Enter birthday in format YYYY-mm-dd')


    def __str__(self):
        return f"Contact name: {self.name.value}, phones:{'; '.join(p.value for p in self.phones)} {'; Birthday '+ str(self.__birthday.value) if self.__birthday.value else '' }"


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


def main():
    book = AddressBook()


# ========================================
if __name__ == "__main__":
    main()




    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone = ("1234567890")
    john_record.add_phone = ("5555555555")
    john_record.add_phone = ("666 666-66-+66")
    john_record.add_phone = ("erty")
    # add birthday
    john_record.add_birthday = ("1200.12.10")
    john_record.add_birthday = ("12-13-1990")
    john_record.add_birthday = ("1990-11-15")
    print(john_record.birthday )
    john_record.days_to_birthday()


    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone ="9876543210"
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




