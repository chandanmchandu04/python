class person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

def my(person):
    print(person.name)
    print(person.gender)
    print(person.age)
    return "person details printed successfully"

# Pass by reference method
def create_new_person(name, gender, age):
    return person(name, gender, age)

p = person("Bharath","male","23")
print(my(p))

my1 = create_new_person("charan","male","20")
print(my1.name)
print(my1.gender)
print(my1.age)

# double underscore is used to make method or variable private
# In python we cannot make anything completely private   
class Bankaccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposite(self, amount):
        self.__balance = self.__balance + amount
        print("Total deposite amount is",self.__balance)

    def withdraw(self, amount):
        if amount >= self.__balance:
            print("Balance insufficent")
        else:
            self.__balance = self.__balance - amount
            print(f'You  withdrawl is {amount} and remaining amount is {self.__balance}')

    def check_balance(self):
        return self.__balance

Chandan = Bankaccount("908880",20000)
Chandan.deposite(10000)
print(Chandan.check_balance())
Chandan.withdraw(3000)
print(Chandan.check_balance())
Chandan.check_balance()

Chandan = Bankaccount("1234",100000)
print(Chandan._Bankaccount__balance)
print(Chandan.deposite(200000))

# Getter() and Setter()
class car:
    def __init__(self, year, brand, name, speed):
        self.year = year
        self.model = brand
        self.name = name
        self.__speed = speed

    def set_speed(self, speed):
        self.__speed = 0 if speed < 0 else speed

    def get_speed(self):
        return self.__speed
    
c = car(2020, "toyata", "supra", 145)
print(c._car__speed)
c.set_speed(230)
print(c.get_speed())

    