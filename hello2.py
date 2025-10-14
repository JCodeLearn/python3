#! /usr/bin/env python3

'''

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(10))

'''

'''

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

product = reduce(lambda x, y : x * y, numbers)

print(product)

'''

'''

def decorator_function(func):
    def wrapper(*args, **kwargs):
        print("Test begins:")
        func(*args, **kwargs)
        print("Test ends!")
    return func

@decorator_function
def target_function(name):
    print(f"Hello, {name}!")

def decorator_newly(func):
    def wrapper(*args, **kwargs):
        print("New Test Begins:")
        func(*args, **kwargs)
        print("New Test Ends!")
    return wrapper

@decorator_newly
def printInfo(name):
    print(f"Hello, {name}!")

target_function("kali")
print("*"*20)
printInfo("Linda")

'''

def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(5)
def greet(name):
    print(f"Hello, {name}!")

greet("Kali")

