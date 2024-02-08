def unique(list):
    res = []
    for i in range(len(list)):
        if list[i] in res:
            continue
        else:
            res.append(list[i])

    return res
        
list1 = [x for x in map(int, input().split())]

print(unique(list1))