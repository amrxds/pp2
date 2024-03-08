import os

path = os.getcwd()
with os.scandir(path) as it:
    print('dir:')
    for file in it:
        if file.is_dir():
            print(' ', file.name)
            
with os.scandir(path) as it:
    print('file: ')
    for file in it:
        if not file.is_dir():
            print(' ', file.name)
