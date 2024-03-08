import os

path = 'C:\\Users\\Пользователь\\Desktop\\Python\\lecture6\\dir-and-files'

if os.access(path, mode=os.EX_OK):
    os.remove(path)