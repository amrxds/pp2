def isPalindrome(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - 1 - i]:
            return False
    return True

x = input()
print(isPalindrome(x))