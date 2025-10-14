#! /usr/bin/env python3
 
# 函数形式类装饰器
'''

def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def _getattr_(self, name): # I don't know the function of this method.
            return getattr(self.wrapped, name)
        
        def display(self):
            print(f"调用{cls.__name__}.display()之前")
            self.wrapped.display() 
            print(f"调用{cls.__name__}.display()之后")
    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")

obj = MyClass()
obj.display() 

'''

'''

# 类形式装饰器
class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("Database 初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)

'''

'''

# 内置装饰器
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method of MyClass!")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(obj.name)

'''

def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
