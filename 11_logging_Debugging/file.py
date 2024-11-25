f = open('test.txt','w')
f.write("This is my new file")
f.close()

with open('test1.txt','w') as f1:
     f1.write("this is my first content")
    


# def func():
#     return lambda a : a ** 2
# print(func()(2))

# S = "This is a lambda function"
# l = lambda s : 'a' in S
# print(l(S))

