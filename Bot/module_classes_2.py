from collections import UserDict
from string import ascii_letters
from datetime import datetime, timedelta
import os
import locale
locale.setlocale(locale.LC_ALL, "")



class Fields:
    __name = None
    __phone = None
    __email = None
    __datebirth = None


class Name(Fields):

    def __init__(self):
        self.__name = ''

    UKR_LETTERS = 'йцукенгшщзхїфівапролджєячсмитьбю.-_ '
    UKR_LETTERS_UP = UKR_LETTERS.upper()
    collection_letters = ascii_letters + UKR_LETTERS + UKR_LETTERS_UP

    def __init__(self):
        self.__name = ''

    # Перевірка імені контакта
    @classmethod
    def verify_name(cls, name):
        if len(name.strip(cls.collection_letters)) != 0:
            res = name.strip(cls.collection_letters)
            return res
        elif name == '':
            return ''
        else:
            return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


class Phone(Fields):

    def __init__(self):
        self.__phone = ['No phone']

    # Перевірка номера телефону
    @staticmethod
    def verify_phone(number):
        while True:
            if len(number) == 0:
                False
                return 'No Phone'
            if number[0] != '+' or len(number) < 13 or number[1:].isdigit() == False:
                return False
            else:
                False
                return number

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, number):
        if number != '':
            list_number = number.split(',')
            for i in list_number:
                if i != 'No phone':
                    self.__phone.append(i)
                    if self.__phone[0] == 'No phone':
                        self.__phone.pop(0)

    def phone_del(self, number):
        self.__phone.pop(self.__phone.index(number))


class Email(Fields):

    def __init__(self):
        self.__email = ['No email']

    # Перевірка e-mail
    @staticmethod
    def veryfi_email(email):
        while True:
            if len(email) == 0:
                False
                return 'No email'
            if email.find('@') == -1:
                return False
            else:
                False
                return True

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if email != '':
            self.__email.append(email)
            if self.__email[0] == 'No email':
                self.__email.pop(0)

    def email_del(self, email):
        self.__email.pop(self.__email.index(email))


class DateBirth(Fields):

    def __init__(self):
        self.__datebirth = 'No date'

    # Перевірка дати народження
    @staticmethod
    def veryfi_date(date_birth):
        while True:
            if len(date_birth) == 0:
                False
                return 'No date'
            if 10 < len(date_birth) < 10 or (date_birth[2] or date_birth[5]) != '-':
                return False
            else:
                if datetime.strptime(date_birth, r'%d-%m-%Y').date().year > datetime.today().date().year:
                    return 'back to the Future'
                else:
                    False
                    return True

    @property
    def date_birth(self):
        return self.__datebirth

    @date_birth.setter
    def date_birth(self, date_birth):
        if self.__datebirth != '':
            self.__datebirth = date_birth

    @date_birth.deleter
    def date_birth(self):
        if self.__datebirth != 'No date' and len(self.__datebirth) != 0:
            self.__datebirth = 'No date'


class AddresBook(UserDict):
    pass


class Record:
    def __init__(self) -> None:
        self.book = AddresBook()
        self.name = Name()
        self.phone = Phone()
        self.email = Email()
        self.date_birth = DateBirth()
        self.fill_book()

    # Заповнюємо словник існуючими контактами при запуску програми
    def fill_book(self):
        try:
            file_book = open('phonebook.msf')
            line_count = sum(1 for line in open('phonebook.msf'))

            if line_count > 0:
                for i in file_book:
                    res = i.replace('\n', '').replace(':', ';').split(';')
                    self.name = Name()
                    self.name.name = res[0]
                    self.phone = Phone()
                    self.email = Email()
                    self.date_birth = DateBirth()

                    for y in res[1].split(','):
                        self.phone.phone = y
                    for u in res[2].split(','):
                        self.email.email = u
                    self.date_birth.date_birth = res[3]
                    self.book.data.update({self.name.name: [{'phone': self.phone.phone},
                                                            {'email': self.email.email}, {'date_birth': self.date_birth.date_birth}]})

            file_book.close()
        except FileNotFoundError:
            file_book = open('phonebook.msf', 'w')
            file_book.close()
            self.fill_book()

    # Додавання запису у книгу
    def add_record(self, name, phone=[], email=[], date_birth=''):

        record = [{'phone': phone}, {'email': email},
                  {'date birth': date_birth}]
        self.add_record_book(name, record)
        with open('phonebook.msf', 'a+') as fh:
            fh.write(name + ':' + ','.join(phone) + ';' +
                     (',').join(email) + ';' + date_birth)
            fh.write('\n')
        return True

    def add_record_book(self, name, record):
        self.book.data.update({name: record})

    # Друк списку усіх контактів
    def show_all_record(self):

        if len(self.book) == 0:
            print('Phone book is empty')
        else:
            os.system('CLS')
            print('='*10, 'Contact list', '='*10)
            for name_book, number_book in self.book.items():
                print(name_book)
                for i in number_book:
                    for key, value in i.items():
                        if type(value) == list:
                            print(key, ":", (',').join(value))
                        else:
                            print(key, ":", value)
                print("*" * 34)

    # Видалення запису з книги
    def delete_record(self, name_contact):

        for name_search in self.book.keys():
            if name_contact == name_search:
                self.book.pop(name_search)
                break
        with open('phonebook.msf', 'w') as fh:
            for i, y in self.book.items():
                rec = []
                for a in y:
                    if type(list(a.values())[0]) != str:
                        rec.append(','.join(list(a.values())[0]))
                    else:
                        rec.append(list(a.values())[0])
                        fh.write(i + ':' + ';'.join(rec))
                        fh.write('\n')

    # Пошук існуючого контакту, або контактів у довіднику
    def search_kontakts(self, name_contact):
        res_search = {}

        for kontakt, num_tel in self.book.items():
            if name_contact in kontakt.lower():
                res_search.update({kontakt: num_tel})

        return res_search

    # Зміна реквізиту контакта
    def change_record(self, name_search, new_value, name_value):

        for name_book, value_book in self.book.items():

            if name_search == name_book:

                new_phone = Phone()
                for t in list(value_book[0].values())[0]:
                    if t != 'No phone':
                        new_phone.phone = t
                if name_value == 'phone':
                    if Phone.verify_phone(new_value):
                        new_phone.phone = new_value

                new_mail = Email()
                for i in list(value_book[1].values())[0]:
                    if i != 'No email':
                        new_mail.email = i
                if name_value == 'email':
                    if Email.veryfi_email(new_value):
                        new_mail.email = new_value

                if name_value == 'date_birth':
                    if DateBirth.veryfi_date(new_value):
                        self.date_birth.date_birth = new_value

                record = [{'phone': new_phone.phone}, {'email': new_mail.email},
                          {'date birth': self.date_birth.date_birth}]
                self.book.update({name_search: record})
                os.system('CLS')

                with open('phonebook.msf', 'w') as fh:

                    for i, y in self.book.items():
                        rec = []
                        for a in y:
                            if type(list(a.values())[0]) != str:
                                rec.append(','.join(list(a.values())[0]))
                            else:
                                rec.append(list(a.values())[0])

                        fh.write(i + ' : ' + ';'.join(rec))
                        fh.write('\n')
        return True

    # Збираємо список юбілярів

    def anniversaries_in_the_week(self, now_day, date_end):
        dict_birth_in_week = {}

        for name, record in self.book.items():
            for dct in record:
                for key, value in dct.items():
                    if key == 'date_birth':
                        date_b = value

            date_b = value.split(
                '-')[0] + '-' + value.split('-')[1] + '-' + now_day.strftime('%Y')
            date_b = datetime.strptime(date_b, '%d-%m-%Y')

            if datetime.isoweekday(date_b) == 6:
                date_b += timedelta(2)
            elif datetime.isoweekday(date_b) == 7:
                date_b += timedelta(1)

            day_in_week = date_b.strftime('%A')

            if now_day <= date_b <= date_end:

                rez = dict_birth_in_week.get(day_in_week)
                if rez == None:
                    dict_birth_in_week.update({day_in_week: [name]})
                else:
                    rez.append(name)
                    dict_birth_in_week.update({day_in_week: rez})

        return dict_birth_in_week

    # Отримуємо поточну дату
    @staticmethod
    def now_days():
        now_date = datetime.now()
        return now_date

    # Отримуємо кінцеву дату аналізу
    @staticmethod
    def delta_dates(now_day):
        delta_dates = timedelta(7)
        date_end = now_day + delta_dates
        return date_end


    @staticmethod
    def print_result(res_jubilars):
        for key, value in res_jubilars.items():
            a = (',  ').join(value)
            print(key, ' : ', a)


    #основна функція друку списку юбілярів
    def get_jubilars(self):

        now_day = self.now_days()

        date_end = self.delta_dates(now_day)

        res_jubilars = self.anniversaries_in_the_week(now_day, date_end)

        self.print_result(res_jubilars)
