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
    lilo = input()
    list = lilo.split()

    for x in list:
        filter_prime(int(x))
        
        if  filter_prime(int(x)) == False:
            print(x)

input_list()