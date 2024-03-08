p = 1
def f(x):
    global p 
    p = p * x
    return x

l = [1,2,3,4,5]
list(map(f,l))
print(p)


l1 = [1,2,3,4,5]
print(eval("*".join(str(item) for item in l1)))
