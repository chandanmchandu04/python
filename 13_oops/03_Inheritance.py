class test:
    def __init__(self, name):
        self.name = "vijay"

    def test_1(self):
        return "This is my first class"

child = test("vijay")
print(child.name)


#CONSTRUCTOR
class phone:

    def __init__(self, price, brand):
        print("Inside the constructor")
        self.price = price
        self.brand = brand

    def buy(self):
        print("Purchasing a new phone")

    def __str__(self):
        return f"phone: {self.brand}, price: {self.price}"

class mobilephone(phone):
    pass

s = mobilephone(100000, "apple")
print(s)

# PRIVATE MEMBERS

class device:
    def __init__(self, cost, manufacturer, camera):
        self.__cost = cost
        self.__manufacturer = manufacturer
        self.camera = camera
    #getter function
    def get_cost(self):
        return self.__cost

    def get_manufacturer(self):
        return self.__manufacturer

class mobile(device):
    #getter function
    def check_cost(self):
        print(self.get_cost())

    def check_manufacturer(self):
        print(self.get_manufacturer())

m = mobile(2024, "samsung", "dslr")
print(m.get_cost())
# m.check_cost()
print(m.get_manufacturer())
# m.check_manufacturer()

# SUPER()
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name,self.age)

class student(person):
    def __init__(self, name, age, rollno):
        self.sName = name
        self.sAge = age
        self.rollno = rollno

        super().__init__("Dhanveer", 25)
        return 

    def displayInfo(self):
        print(self.sName,self.sAge,self.rollno)

obj = student("varun",18,101)
print(obj.display())
print(obj.displayInfo())      

# STATIC METHOD
class student:
    def student_details(self,name,email):
        print(name,email)

    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)
 
    @classmethod
    def class_name(cls, class_name):
        cls.mentor_class(["gopi", "bhavani"])

    # def mentor(self,mentor_list):
    #     print(mentor_list)

student.mentor_class(["prabhas", "Akash"])
stu1 = student()
print(stu1)

student.class_name(["bhavani"])
stu2 = student()
print(stu2)