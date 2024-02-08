def filter_prime(intt):
    i = 2
    while i < intt:
        if intt == 2:
             return False
             break 
        if intt%i == 0:
                return True
        else:
                return False
                break
        

def input_list():
   list1 = [int(n) for n in input().split()]

   for x in list1:
        filter_prime(x)
        if filter_prime(x) == False:
            print(x)

input_list()

     
