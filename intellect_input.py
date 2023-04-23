
COMMANDS = ['Add', 'Change', 'Delete', 'Create', 'Exit', 'Note', 'AddressBook']


def recognize_command(text):
    res_dict = {}
    for i in COMMANDS:
        percent = 0
        for y in list(text.lower()):
            if len(list(text)) <= len(i):
                if y in list(i.lower()):
                    percent += 100 / len(list(i))
                res_dict[i] = percent
    return max(res_dict, key=res_dict.get)


if __name__ == '__main__':
    status = True
    while status == True:
        print('Enter the command')
        text = input('>>>>  ')
        res_1 = recognize_command(text)
        if res_1 == None:
            print('Command not recognized. Re-enter? (yes/no)')
            choice = input('>>>>  ')
            if choice.lower() == 'no':
                break           
        else:
            print(f'Command entered  = "{res_1}"')
            print('Re-enter command? (yes/no)')
            choice = input('>>>>  ')
            if choice.lower() == 'no':
                status = False
