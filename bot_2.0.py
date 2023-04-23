import export_func as basic
import modul_classes_2 as class_exp
import time


book = class_exp.Record()

def main_menu():

    basic.os.system('CLS')
    print('==== main menu ====')
    print('How can I help you?')
    print('1. - Phonebook\n2. - Calendar jubilars\n3. - Exit\nYour chois:')

    chois = input('>>>>  ')
    if chois == '1':
        phone_menu()
    elif chois == '2':
        calendar_menu()
    else:
        basic.input_output('end')


def phone_menu():

    basic.os.system('CLS')
    print('==== phonebook menu ====')
    print('add - adding a contact to the phonebook\nchange - change an existing contact'
          '\nphone - contact information by name\nshow all - list of all contacts\n'
          'del - deleting a contact from the phonebook\nexit - exit to main menu'
          '\nYour chois:')

    
    chois = input('>>>>  ').lower()
    if chois == 'add':
        basic.os.system('CLS')
        print('==== adding contact ===')
        
        print('Enter contact name(Name Surname (cannot be empty))')
        name_contact = input('>>>> ')
        res = basic.check_name(name_contact)
        if res[0] == True:
            name = class_exp.Name()
            name.name = res[1]
            print(f'Name {res[1]} added sucsess')
        print('=' * 30)
        print('Add additional data ? (phone number, email, date of birth) (yes/no)')
        chois = input('>>>>  ')
        if chois.lower() == 'yes':
            print('Enter phone number \nun the format +380672972960 (may be empty)')
            number_contact = input('>>>>  ')
            res = basic.check_number(number_contact)
            if res[0] == True and len(res[1]) > 0:
                phone = class_exp.Phone()
                phone.phone = res[1]
                print(f'Phone number {res[1]} added sucsess')

            print('Add email address un the format "post@mail.com" (may be empty)')
            email_contact = input('>>>>  ')
            res = basic.check_email(email_contact)
            if res[0] == True and len(res[1]) > 0:
                email = class_exp.Email()
                email.email = res[1]
                print(f'E-mail {res[1]} added sucsess')

            print("Add contact's date of the birth un the format 'dd-mm-yyyy'(may be empty)")
            date_birth = input('>>>>  ')
            res = basic.check_birthdate(date_birth)
            if res[0] == True and len(res[1]) > 0:
                date_birth = class_exp.DateBirth()
                date_birth.date_birth = res[1]
                print(f'Date of the birth "{res[1]}" added sucsess')
            
        else:
            phone = class_exp.Phone()            
            email = class_exp.Email()
            date_birth = class_exp.DateBirth()
                        
        book.add_record(name.name, phone.phone, email.email, date_birth.date_birth)
        print(f'Contact details "{name.name}" added successfully')
        time.sleep(3)
        phone_menu()           


    elif chois == 'change':
        status = True        
        
        while status == True:
            basic.os.system('CLS')
            print('==== contact change ====')
            print('Enter contact name')
            name_contact = input('>>>>  ')
            result = book.search_kontakts(name_contact)
            if len(result) == 0:
                print(f'Name "{name_contact}" not found. Re-enter? ( yes / no)')
                chois_1 = input ('>>>>  ')
                if chois_1.lower() == 'no':
                    status =False
                    phone_menu()
                
            else:  
                basic.os.system('CLS')
                print('==== contact change ====')
                count = 1
                for name, number in result.items():
                    count_1 = 1
                    print(count,' : ',name)
                    for i in number:                        
                        for key, value in i.items():                            
                            if type(value) == list:
                                print(count_1, ' : ',key, " : ", (', ').join(value))
                                count_1 +=1
                            else:
                                print(count_1, ' : ',key, " : ", value)
                    print("*" * 34)
                    count_1 =1
                    count +=1

                if count > 2:
                    print('Enter the number of the contact you want to change')
                    num_change = input('>>>>  ')
                    print('Enter the number of the value contact you want to change')
                    num_value = input('>>>>  ')
                else:
                    num_change = 1 
                    print('Enter the number of the value contact you want to change')
                    num_value = input('>>>>  ')
                print(
                    f'Enter a new value "{list(list(result.values())[int(num_change)-1][int(num_value) -1].keys())[0]}" for contact "{list(result.keys())[int(num_change)-1]}"')
                new_value = input('>>>>  ')
                book.change_record(list(result.keys())[int(num_change)-1], new_value, list(
                    list(result.values())[int(num_change)-1][int(num_value) - 1].keys())[0])
                print(
                    f'Value "{new_value}" added to contact "{list(result.keys())[int(num_change)-1]}"')
                time.sleep(3)
                phone_menu()



            

    elif chois == 'phone':

        class_exp.os.system('CLS')       

        status = True
        while status == True:
            print('==== contact information ====')
            print('enter contact name')
            name_contact = input ('>>>>  ')
            result_names = book.search_kontakts(name_contact)

            class_exp.os.system('CLS')
            print('='*10, 'Result search', '='*10)
            for name_book, number_book in result_names.items():
                print(name_book)
                for i in number_book:
                    for key, value in i.items():
                        if type(value) == list:
                            print(key, " : ", (', ').join(value))
                        else:
                            print(key, " : ", value)
                print("*" * 34)
            print('Return in phone menu ? (yes / no)')
            chois = input('>>>>  ')
            if chois.lower() == 'yes':
                status = False
                phone_menu()
            else:
                class_exp.os.system('CLS')

            if len(result_names) == 0:
                print('Contacts with such data were not found. Repeat search? (yes/no)')
                response = input('>>>>  ')
                if response.lower() == 'no':
                    search = False
                    phone_menu()
            
                

        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'show all':
        book.show_all_record()
        print('Return in menu phonebook ?(yes/no)')
        if input('>>>>  ').lower() == 'yes':
            phone_menu()
        else:
            main_menu()

    elif chois == 'del':
        status = True
        while status == True: 
            basic.os.system('CLS')
            print('==== delete change ====')
            print('Enter contact name')
            name_contact = input('>>>>  ')
            result = book.search_kontakts(name_contact)    
            if len(result) == 0:
                print('Contacts with such data were not found. Repeat search? (yes/no)')
                chois = input('>>>>  ')
                if chois.lower() == 'no': 
                    status = False               
                    phone_menu()
            else:
                count = 1
                count = 1
                for name, number in result.items():
                        count_1 = 1
                        print(count, ' : ', name)
                        for i in number:
                            for key, value in i.items():
                                if type(value) == list:
                                    print(count_1, ' : ', key,
                                            " : ", (', ').join(value))
                                    count_1 += 1
                                else:
                                    print(count_1, ' : ', key, " : ", value)
                        print("*" * 34)
                        count_1 = 1
                        count += 1
                if count >2:
                    print('Enter the number of the contact you want to delete')
                    num_change = input('>>>>  ')
                else:
                    num_change = 1
                print(
                    f'Contact "{list(result.keys())[int(num_change)-1]}" entry will be deleted from the phonebook.(yes/no)\nYour choise')
                chois = input('>>>>  ')
                if chois.lower() == 'yes':
                    book.delete_record(list(result.keys())[int(num_change)-1])
                print(
                    f'Record "{list(result.keys())[int(num_change)-1]}" deleted from phone book')
                print('Return in menu phonebook ?(yes/no)')
                chois = input('>>>>  ')
                if chois.lower() == 'yes':
                    status = False                
                    phone_menu()
                else:
                    status = False
                    main_menu()                    

    elif chois == 'exit':
        main_menu()

    else:
        print('Incorrect chois...')
        time.sleep(3)
        phone_menu() 
        

def calendar_menu():
    class_exp.os.system('CLS')
    book.get_jubilars()
    print('='*30)
    print('Return in main menu (yes/no)')
    chois_2 = input('>>>>  ')
    if chois_2.lower() == 'yes':
        main_menu()
    else:
        basic.input_output('goodbye')


def __main__():
    class_exp.os.system('CLS')
    print('Hello! I am a bot.\nEnter "hello" to get started or any other word to exit.')
    chois = input('>>>>  ').lower()
    chois = basic.input_output(chois)
    if chois == True:        
        main_menu()

if __name__ == '__main__':
    __main__()
