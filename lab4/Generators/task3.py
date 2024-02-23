class by3and4:
    def __init__(self, end):
        self.end = int(end)
    
    def __iter__(self):
        self.start = 0
        return self
    
    def __next__(self):
        nxt = self.start
        self.start += 12
        
        if nxt <= self.end:
            if nxt % 12 == 0:
                return nxt
        else:
            raise StopIteration

N = int(input())

x = by3and4(N)
x = iter(x)
for i in x:
    print(i)