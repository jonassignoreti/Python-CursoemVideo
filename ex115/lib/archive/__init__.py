from ex115.lib.interface import *

def file_exist(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def create_file(file):
    try:
        a = open(file, 'wt+')
        a.close()
    except:
        error(f'Error creating file {name}')
    else:
        print(f'File {name} created successfully!')


def read_file(file):
    global size
    try:
        a = open(file, 'rt')
    except:
        error('ERROR READING DE FILE')
    else:
        return a.readlines()
    finally:
        a.close()


def write_file(file, name='unknown', age='unknown'):
    try:
        a = open(file, 'at')
    except:
        error(f'ERROR opening the file {file}')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            error('ERROR, new person registration fail')
        else:
            print(f'{name} was registered successfully')
        finally:
            a.close()


def clean_file(file):
    try:
        a = open(file, 'w+')
    except:
        error(f'ERROR, file {file} was not cleaned')
    else:
        print(f'File {file} cleaned successfully')
    finally:
        a.close()
