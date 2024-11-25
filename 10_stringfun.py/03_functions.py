def sub(a = 10, b = 20):
    c = a - b
    print(c)
sub()#default argument

def add(a , b):
    c = a + b
    print(c)
add(10, 40)#positional argument

def add(a , b):
    c = a + b
    print(c)
add(b = 40, a = 4)#keyword argument

def fun(*args): #SINGLE ARGUMENT  #TUPLE
    result = sum(args)
    print(result)
fun(2, 3, 32, 44, 99, 69, 79, 89)

def function1(a, b, *pril, **pri): #SINGLE AND DOUBLE ARGUMENT  #DICTIONARY
    return a, b, pril, pri
result = function1(1, 2, 1, 3, 4, 5, 66, 77, name ="RCB", age = 16)
print(result)

#OUTPUT
def add(a,b):
    '''it will add two number''' #DOCTYPE
    c = a + b
    print(c)
add(50,50)
# print always returns none type 
# we cannot convert it 


