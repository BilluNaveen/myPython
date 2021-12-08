class Person:
    # body of the constructor
    # we are directly passing arguments class
    def __init__(self,name,age):
        self.name=name
        self.age=age
name=input()
age=int(input())
obj=Person(name,age)

# does not use constructor, we have pass by method arguments

class Person1:
    def method (self,name,age):
        self.name=name
        self.age=age
obj1=Person1()
obj1.method(name,age)