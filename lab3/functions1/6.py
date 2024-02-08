def reverse(string):
    words = string.split()
    newwords = words[::-1]
    sen = ' '.join(newwords)
    print(sen)

reverse("We are ready")