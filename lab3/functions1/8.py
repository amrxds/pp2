
def spy_games(arr):
    return '007' in ''.join(str(i) for i in arr)
listin = input()
list1 = listin.split()
print(spy_games(list1))