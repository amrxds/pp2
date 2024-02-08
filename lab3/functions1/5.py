
import itertools

def Permutation(string):
    
	x = ["".join(i) for i in itertools.permutations(string)]

	print(x)

string = input()

Permutation(string)