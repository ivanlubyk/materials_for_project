import time

COMMANDS = ['add', 'change', 'del', 'create', 'exit', 'note',
            'Phonebook', 'Calendar jubilars', '1', '2', '3', 'phone', 'show all']


def recognize_command():
    status = True
    while status == True:
        print('Enter the command')
        text = input('>>>>  ')
        res_dict = {}
        for i in COMMANDS:
            percent = 0
            for y in list(text.lower()):
                if len(list(text)) <= len(i):
                    if y in list(i.lower()):
                        percent += 100 / len(list(i))
                    res_dict[i] = percent
        choice = max(res_dict, key=res_dict.get)
        if sum(res_dict.values()) == 0:
            print('Command not recognized. Re-enter? (yes/no)')
            choice_1 = input('>>>>  ')
            if choice_1.lower() == 'no':
                status = False
        else:
            print(f'Command recognized as : "{choice}"')
            time.sleep(3)
            status = False            
    return choice

    
