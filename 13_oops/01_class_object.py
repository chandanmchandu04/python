#Creating a class
class test:
    pass

#creating of object
obj = test()

A = test()
print(type(test))
print(type(A))

class oops:

    a = 10
    b = 20

    def welcome_msg(self):
        print("welcome to oops concept")

obj = oops()
obj.welcome_msg()
print(obj.a)
print(obj.b)

# what we can pass in class?
# We call variable as attribute inside a class and function as method.

# def __init__(self):
# As we create obj it will execute.
# init  helps to pass the value inside the class.
# We don't need to call the constructor.

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)
        self.my()

    def my(self):
        print("It executes due to constructor")

obj = person("viratkohli", 35)
print(obj)

# Parameterised Constructor.

class person:
    def __init__(self, name, age):
        print(id(self))
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)
        self.my()

    def my(self):
        print("It executes due to constructor")

obj2 = person("Rohith sharma", 38)
print(obj2)

# NonParameterised Constructor.

class person:
    def __init__(self):
        print(id(self))
        self.name = "Hardhik"
        self.age = 33
        print(self.name)
        print(self.age)
        self.my()

    def my(self):
        print("It executes due to constructor")

obj1 = person()
print(obj1)


# Magic Method
# Are used for doing specific task on object.

#project on class and object
class Bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance + amount
        print("Total deposite amount is",self.balance)

    def withdraw(self, amount):
        if amount >= self.balance:
            print("Balance insufficent")
        else:
            self.balance = self.balance - amount
            print(f'You  withdrawl is {amount} and remaining amount is {self.balance}')

    def check_balance(self):
        return self.balance

Chandan = Bankaccount("908880",20000)
Chandan.deposite(10000)
print(Chandan.check_balance())
Chandan.withdraw(3000)
print(Chandan.check_balance())
Chandan.check_balance()