class MyEvenNumbers:
    def __init__(self, end_num):
        self.end_num = end_num
        
    def __iter__(self):
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter <= self.end_num:
            current_num = self.counter
            self.counter += 1

            if current_num % 2 == 0: 
                return current_num
            else:
                return self.__next__() 
        else:
            raise StopIteration
    
    def get_size(self):
        return self.end_num
          
    
my_generator = MyEvenNumbers(100)
my_iterator = iter(my_generator)

for idx, obj in enumerate(my_iterator):
    if idx != int(my_generator.get_size() / 2):
        print(f'{obj}', end=", ")
    else:
        print(obj)
