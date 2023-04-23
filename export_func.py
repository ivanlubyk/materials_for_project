import modul_classes_2 as class_exp
import os, calendar


# Перевірка імені контакта на коректність
def check_name(name):
    while True:
        if isinstance(class_exp.Name.verify_name(name), str):
            print(
                f'The input contains invalid characters "{class_exp.Name.verify_name(name)}". Re-enter')
            print(
                'Only characters of the Ukrainian\nor Latin alphabet can be used in the name and "-"')
            if class_exp.Name.verify_name(name) == '':
                print('Field cannot be empty')
            name = input('>>>>  ')
            class_exp.Name.verify_name(name)
        else:
            False
        return (True, name)


#Перевірка номера контакта на коректність
def check_number(number):
    if not class_exp.Phone.verify_phone(number):
        print(
            f'The entered number {number} does not match the format\n+380672972960\nRe-enter (Or leave the field blank)')
        number = input('>>>>  ')
        class_exp.Phone.verify_phone(number)
    else:
        if number == '':
            number = 'No phone'
    return (True, number)

#Перевірка email на коректність
def check_email(email):
    if not class_exp.Email.veryfi_email(email):
        print(
            f'The data "{email}" entered is not e-mail. Re-enter (Or leave the field blank)')
        email = input('>>>>  ')
        class_exp.Email.veryfi_email(email)
    else:
        if email == '':
            email = 'No email'
    return (True, email)


#Перевірка дати народження на коректність
def check_birthdate (birthdate):
    if class_exp.DateBirth.veryfi_date(birthdate) == 'back to the Future':
        print('This date has not yet arrived. Re-enter')
        birthdate = input('>>>>  ')
        class_exp.DateBirth.veryfi_date(birthdate)
    if not class_exp.DateBirth.veryfi_date(birthdate):
        print('Invalid date entered (sample - "dd-mm-yyyy")')
        date_birth = input('Re-enter >>>>  ')
        class_exp.DateBirth.veryfi_date(date_birth)
    else:        
        if birthdate == '':
            date_birth = 'No date'
            return (True, date_birth)
        else:
            return (True, birthdate)



#Реакція на ввод користувача у головному меню
def input_output(text_user):

    if text_user == 'hello':
        return True
    else:        
        print('=== GoobBye ! ===')
        return False