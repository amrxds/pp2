class Numbers:
    def __init__(self, start):
        self.start = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        cont = self.start
        self.start -= 1
        
        if cont >= 0:
            return cont
        else:
            raise StopIteration
        

itnum = Numbers(10)
itnum = iter(itnum)

for i in itnum:
    print(i)