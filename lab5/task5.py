import re

pattern = r'a\w+b\b'

s = ["alolb", "alold", "lol123lolb"]

for x in s:
    if re.search(pattern, x):
        print(x)