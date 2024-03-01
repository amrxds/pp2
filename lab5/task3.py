import re

pattern = r'(\b[a-z]+_.+\b)'

s = ["Amirkhan", "hello_world", "kbtu"]

for x in s:
    if re.match(pattern, x):
        print(x)
