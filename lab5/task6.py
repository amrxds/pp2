import re 

s = "Привет, мир. Как дела?"

result = re.sub('[, .]', ':', s)

print(result)