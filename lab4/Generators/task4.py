class Numbers:
    def __init__(self, start=0, end=0):
        self.__start = start
        self.__end = end

    def __iter__(self):
        self.__current = self.__start
        return self

    def __next__(self):
        if self.__current <= self.__end:
            current_value = self.__current
            self.__current += 1
            return current_value
        else:
            raise StopIteration

    def squares(self):
        for number in self:
            yield number ** 2


test_numbers = Numbers(0, 10)

for squared_number in test_numbers.squares():
    print(squared_number)
    