username = "tesla"

def func() :
    username = "maruti"
    print(username)


func()

def func3():
    global x
    x = 23
func3()
print(x)

def f1():
    x = 888
    def f2():
        print(x)
    return f2()
myResult = f1()
myResult() 