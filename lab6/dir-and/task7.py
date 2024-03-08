with open('some', 'r') as file:
    file_contents = file.read()

with open('some_copy', 'w') as file_copy:
    file_copy.write(file_contents)
