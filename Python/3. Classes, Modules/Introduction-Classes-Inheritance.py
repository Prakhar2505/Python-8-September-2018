# introduction to Classes -
class MathsFunction:

    def __init__(self, a, b):
        self.var_1 = a
        self.var_2 = b

    def addition(self):
        result = self.var_1 + self.var_2
        print(result)

obj = MathsFunction(10, 20)
obj.addition()

class MathFunction:

    def __init__(self,a,b):
        self.var1=int(a)
        self.var2=int(b)

    def sum(self):
        result=self.var1+self.var2
        print(result)

a=input("Enter 1st no")
b=input("Enter 2nd no")

obj=MathFunction(a,b)
obj.sum()


# Introduction to Inheritance
class BaseClass:

    def __init__(self):
        self.var_1 = 2
        print("Base Class")

    def helloFxn(self, a = 10):
        print("Hello Inside base class")

class DerivedClass(BaseClass):

    def __init__(self):
        super().__init__()
        print("Derived Class")
        super().helloFxn(a=20)
        self.helloFxn()

    def helloFxn(self):
        print("Hello inside derived class")

obj = DerivedClass()


## Students Class

class Student:
    def __init__(self, name, address="Dehradun", phone = 0):
        self.name = name
        self.address = address
        self.phone = phone
        print("Welcome to Brillica Services")

    def display_data(self):
        print("Printing students details")
        print(self.name)
        print(self.address)
        print(self.phone)

name = input('Enter your name')
address = input('Enter your address')
phone = input('Enter your phone number')
if ((len(address)>1) & (len(phone)>1)):
    phone = int(phone)
    obj = Student(name=name, address=address, phone=phone)
    obj.display_data()
elif (len(address)>1 & (len(phone)==0)):
    obj = Student(name, address)
    obj.display_data()
elif (len(phone)>1 & (len(address)==0)):
    phone = int(phone)
    obj = Student(name=name, phone=phone)
    obj.display_data()
else:
    obj = Student(name)
    obj.display_data()
