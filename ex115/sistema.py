from ex115.lib.interface import *
from ex115.lib.archive import *
from time import sleep
size = 40

archive = 'ex115b.txt'
if file_exist(archive):
    print('file found successfully')
else:
    create_file(archive)

txt_white(f=1)
back_blue(f=1)
title('>>>> ARCHIVE SYSTEM v1.0 <<<<', size)
sleep(1)
while True:
    txt_white(f=1)
    back_red(f=1)
    ans = menu(['View registered people',
                 'Register a new person',
                 'Clean the register',
                 'Exit the system'], size)
    style_negative(f=1)
    txt_white(f=1)
    if ans == 1:
        # View registered people
        title('Registered People', size)
        lst = read_file(archive)
        for p in lst:
            data = p.split(';')
            data[1] = data[1].replace('\n', '')
            print(f'{data[0]:<{size - 8}}{data[1]:>3} anos')
        line(size)
    elif ans == 2:
        # Register a new person
        title('Register a New Person')
        name = str(input('Name: ')).strip()
        age = readInt('Age: ', 'ERROR, type an integer number')
        write_file(archive, name, age)
        line(size)
    elif ans == 3:
        clean_file(archive)
    elif ans == 4:
        print('Exiting the system...')
        sleep(2)
        break
    else:
        error('ERROR!, select a valid option.')
    style_none(f=1)
    sleep(2)
