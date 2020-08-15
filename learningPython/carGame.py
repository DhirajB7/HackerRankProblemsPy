eng = False

while True:
    command = str(input('> ')).lower()
    if command == 'help':
        print('start - to start car')
        print('stop - to stop car')
        print('quit - to quit game')
    elif command == 'start':
        if eng:
            print('ALREADY STARTED')
        else:
            print('STARTED....LETS GO!!!')
            eng = True
    elif command == 'stop':
        if eng:
            print('!!!!!!!!!!!STOPPED!!!!!!!!!!!!!!!!')
            eng=False
        else:
            print('ALREADY STOPPED')
    elif command == 'quit':
        print('BYE BYE NOW')
        break
    else:
        print("I DON'T UNDERSTAND YOU")
