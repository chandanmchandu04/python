#Nested Functions
def call():
    def add(a,b):
        return a + b
    def sub(a,b):
        return a - b
    def mul(a,b):
        return a * b
    def div(a,b):
        return a / b
    return{'add':add, 'sub':sub, 'mul':mul, 'div':div}

print(call()['add'](10,10))
print(call()['mul'](10, 10))

#Higher Order Function
#Functions as a Data type
def hello(a):
    return a**3
print(hello(2))
print(type (hello))

#function returning a function
def hello1():
    def hello2(a):
        return a**3
    return hello2
print(hello1()(4))

def mul(a):
    def mul1(b):
        return a + b
    return mul1
print(mul(2)(3))

#Function as a argument
def operation (a,b,oper):
    return oper(a,b)

def add(a,b):
    return a + b
def mul(a,b):
    return a * b

print(operation(2,3,mul))

#Lambda Function
s = lambda a : a**3
print(s(20))

operation = (lambda a, b : a + b)
print(operation(2,4))

#Map Function
l = [1, 22, 44, 55, 6666, 66667, 888, 89, 8]
print(list(map(lambda x : x**1, l)))

words = ["virat", "rohith", "yuvi"]
print(list(map(lambda word : word.capitalize(), words)))

#reduce function
from functools import reduce
print(l)
print(reduce(lambda x,y : x + y, l)) 

#Iterable and Iterator
import sys
l = [i for i in range (1000000)] #Here we are using list to check the range. more memory storage 
print(sys.getsizeof(l)) 

import sys
l1 = range(1000000000) # here if we go on incresing the number memory storage will be used less.
print(sys.getsizeof(l1))

print('__iter__' in dir(iter(l1)))
print('__next' in dir(iter(l1)))
print('__iter__' in dir(l))
print('__next__' in dir(l))