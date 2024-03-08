data = [1, 2, 3, 4, 5]

with open("file2.txt", "w") as file:
    for item in data:
        file.write(str(item) + "\n")