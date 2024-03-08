with open("some", 'w') as s:
    s.write("Hello\nKbtu!.txt")

with open('some') as file:
    print(len(list(file)))
