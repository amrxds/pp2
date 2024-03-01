def tocamel(string):
    elements = string.split('_')
    x = ''.join(x.capitalize() for x in elements[0:])
    return x


string = input()
c = tocamel(string)
print(c)