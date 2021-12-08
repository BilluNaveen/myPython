class ClassMethod:
    @classmethod
    def method(cls,name,age):
        cls.name=name
        cls.age=age
        print(cls.name,cls.age)

name=input()
age=int(input())
obj=ClassMethod()
obj.method(name,age)
# we are not inistalize arguments
class StaticMethod:
    @staticmethod
    def method1(name,age):
        print(name,age)
    @staticmethod
    def method2():
        print(name)
obj=StaticMethod()
obj.method1(name,age)
obj.method2()