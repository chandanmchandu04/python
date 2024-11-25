def mydeco(func):
    def inner():
        print("Welcome To")
        func()
        print("Live Stream")
    return inner

@mydeco
def hello():
    print("decorators")
hello()
# a = mydeco(hello)
# a()

# decoraters are functions used to modify the behavior of another function without changing its code 
# Example for decoraters 
@mydeco
def hello1():
    print("This is the second function")
hello()


import time
def timer_func(func):
    def time_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end-start)
    
    return time_test_inner
 
@timer_func
def test2():
    print(123456 + 568994)
test2()

# PROPERTY DECORATOR
# GETTER METHOD
class course:
    def __init__(self, course_name, course_price):
        self.__course_name = course_name
        self.course_price = course_price

    @property
    def course_name(self):
        return self.__course_name
    
b = course("Artifical Intellegence", 30000)
print(b.course_name)
print(b.course_price)

# SETTER METHOD
class course:
    def __init__(self, course_name, course_price):
        self.__course_name = course_name
        self.course_price = course_price

    @property
    def course_price_access(self):
        return self.__course_price
    
    @course_price_access.setter
    def course_price_access(self, price):
        if price < 0:
            pass
        else:
            self.__course_price = price

    @course_price_access.deleter
    def del_price_access(self):
        del self.__course_price

b = course("Artifical Intellegence", 30000)
b.course_price = 40000
print(b.course_price)
# del b.del_price_access    