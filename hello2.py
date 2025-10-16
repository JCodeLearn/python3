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

'''

'''

wordsValue = dict(sape=4139, guido=4127, jack=4098)
for k,v in wordsValue.items():
    print(k, v)

'''

'''

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

'''

'''

questions = ['name', 'quest', 'favortie color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

'''

'''

import sys

print("命令行参数如下：")
for i in sys.argv:
    print(i, end=' ')

print()
print('\n\nPython 路径为：', sys.path, '\n')

'''

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
