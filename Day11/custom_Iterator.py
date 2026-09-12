"""
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            number = self.current
            self.current += 1
            return number
        else:
            raise StopIteration

counter = CountUpTo(5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
"""

#CHALLENGE
class EvenNum:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2
    def __iter__(self):
        return self
    def __next__(self):
        while self.current <= self.limit:
            if self.current % 2 == 0:
                even = self.current
                self.current += 1
                return even
            else:
                self.current += 1
        raise StopIteration

even = EvenNum(10)
for number in even:
    print(number)
