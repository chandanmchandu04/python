from abc import ABC, abstractmethod

class shape(ABC):

    def database(self):
        pass

    @abstractmethod
    def display(self):
        pass
      

import abc
class method:

    @abc.abstractmethod
    def student(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass
    
    @abc.abstractmethod
    def student_details(self):
        pass

c = method()

class student_details(method):
    def student_details(self):
        return "These are some of the student details"
    
    def student_marks(self):
        return "Marks of some of the students"
    
    def student(self):
        return "Total number of students with their marks and details"
    


from abc import ABC , abstractmethod

class human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self.name)
        print(self.age)

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def speak(self):
        pass

class Employee(human):
    
    def speak(self):
        print("This is for the Interview basics")

    def work(self):
        print("This is for the task basics")

    def __repr__(self):
        return f"Employee(name={self.name!r}, age={self.age!r})"

s = Employee("Ishan", 23)
print(s)
print(s.speak())
print(s.work())