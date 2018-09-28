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
