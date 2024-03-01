#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
pattern = r'[A-Z][a-z]+'

s = ["aaaalol", "AMIRKHANdossymov", "LOOL", "ASDFasdfASDF"]

for x in s:
    if re.search(pattern, x):
        print(x)


