import re

s = ['abbbbb', 'ab', 'ac', 'fasd']

pattern = r'ab*'
for string in s:
    if re.match(pattern, string):
        print(string)