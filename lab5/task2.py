#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
pattern = r'ab{2,3}$'

s = ["ab", "abbbb", "abbb", "abb", "aba" ]

for x in s:
    if re.match(pattern, x):
        print("Yes", x)
    else:
        print("No", x)