def count(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    return upper_count, lower_count

x = input()

upper , lower = count(x)

print(f"upper {upper}")
print(f"lower {lower}")