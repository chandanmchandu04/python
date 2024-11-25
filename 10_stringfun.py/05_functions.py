#Custom For loop and Range 
#iter()
#next()
#Exception Handling

num = [1, 23, 4, 343, 34, 5]

def myloop(num):
    iterator = iter(num)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
print(myloop(num))

#Range
class Myrange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            value = self.start
            self.start = self.start + self.step
            return value
        else:
            raise StopIteration

r = Myrange(1, 8, 1)
for i in r:
    print(i)