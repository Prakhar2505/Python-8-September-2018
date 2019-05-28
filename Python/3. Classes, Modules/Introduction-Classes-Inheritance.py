# introduction to Classes -
class Student: ## user defined datatype
    def __init__(self, name='Python'): # constructor
        self.name = name
        print("Hello World")

    def welcome(self):
        print(self.name)
        print('Welcome to python programming')

obj = Student('Gurjas')
obj.welcome()
obj1 = Student()
obj1.welcome()


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


## Static -- Students Class

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
    

## Dynamic -- Students Class

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
        
        
students_count = input('Enter the number of records you want')
students_count = int(students_count)
students_records = []
for i in range(students_count):
    print('Enter the details of student:')
    name = input('Enter the name of the student')
    address = input('Enter the address of the student')
    phone = input('Enter the phone number of the student')

    obj : Student
    if ((len(address) > 1) & (len(phone) > 1)):
        phone = int(phone)
        obj = Student(name=name, address=address, phone=phone)
    elif (len(address)>1 & (len(phone)==0)):
        obj = Student(name, address)
    elif (len(phone)>1 & (len(address)==0)):
        phone = int(phone)
        obj = Student(name=name, phone=phone)
    else:
        obj = Student(name)

    students_records.append(obj)

for i in students_records:
    i.display_data()
