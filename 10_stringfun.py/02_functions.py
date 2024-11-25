name = 'fazer'
age = 23
s = 'I am  {} and I am {} and I am very young'
print(s.format(name, age))

s1 = {1, 22, 3, 444, 5, 666, 7778}
print(type(s1))

l = [1, 23, 2, 'hello', 'python', 2 + 3j, 1, 23, 2]
print(l)
 
l1 = [1, 23, 2, 'hello', 'python', 2 + 3j, 1, 23, 2]
print(l1)

l = {1, 23, 2, 'hello', 'python', 2 + 3j, 1, 23, 2}
print((l))
 
my_dict = {'one':1, 'two':2, 'three':3}
print((my_dict))


#SCOPE OF A VARIABLE
y = 5  
def hello():
    x = 3
    global y
    y = y + 1
    print(f"this is my global variable {y}")
    print(3)

print(y)
hello()

# To access through list we use it by declaring index so then we will get the same output in the different way
y = [5]  
def hello():
    x = 3
    y[0] = y[0] + 1
    print(f"this is my global variable {y[0]}")
    print(3)

print(y[0])
hello()