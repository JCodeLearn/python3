#! /usr/bin/env python3
'''

以脚本方式运行，首先先在 python 文件顶部设置如上注释，然后赋值该文件可执行权限，最后就可以像
直接运行可执行文件或 shell 脚本一样运行 python 脚本

'''

# print("Hello, world!")

# 查看当前 python 版本的保留字

'''

在交互式解析器中
import keyword
keyword.kwlist 

'''

"""

python 中的 3 种注释

"""

"""

import sys
x = 'runoob'
sys.stdout.write(x + '\n')

"""

"""

x = "a"
y = "b"

print(x)

print(y)

print('--------')

print(x, end = " ")
print(y, end = " ")

print()


"""

"""

from sys import argv, path

print('Python3 path:', path)

"""

"""

array = 'Hello, This is the python file!'
print(array[2:5])

"""

'''

i = 5
i += 3
print(i)

'''

'''

print(True + 3)

'''

'''

array = "Hello, BOY!"
print(array[1:5:2])

'''

# 字符串切片的步长不能为负数

'''

a = 1
tup1 = ('hello', 1, True, False, a)
tup2 = ('Where to find you ?', 1, 2, 1 + 3j)
tup = tup1 + tup2
print(tup)

print('-'*20)
aList = ["hello", a, True, False]
aList[0:2] = []
print(aList)

'''

'''

tree = {}
tree['one'] = 'Hello, this is a dictionary'
tree[2] = 'Are you Okay?'

print(tree)

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

'''

'''

tree = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(tree)
x = {x: x**2 for x in (2, 4, 6)}
print(x)
y = dict(Runoob=1, Google=2, Taobao=3)
print(y)

'''

'''

x = bytes("hello", encoding="utf-8")
print(x)

'''

'''

a = 10
list = [1, 2, 3, 4, 5]
if (a in list):
    print(" a is in the list!")
if (5 not in list):
    print("5 is not in the list")
else:
    print("5 is in the list")

'''

'''

a = 10
b = 10

if(a is b):
    print("a 和 b 实际上引用的是同一个对象，在 python 中 number 是不可变的")
else:
    print("我说吧， a 和 b 怎么可能引用同一个对象")

if(id(a) == id(b)):
    print("id 函数是用来获取引用对象的内存地址的，然后 a 和 b 实际引用的是同一个对象")
else:
    print("a 和 b 引用的不是同一个对象，还有 is not 的语法结构")

'''

'''

array = "Hello, World!"
if("Hello" in array): 
    print("Hello is the substr of array:\"Hello, World\"")
else:
    print("Hello is not the substr of array:\"Hello, World\"")

'''

'''

name = "Harry Potter"
age = 10
array = "Hello, What's your name? %s\n " \
"What's your age? %d years old!" % (name, age)
print(array)

'''

'''

x = 1
print(f'{x+1=}')

'''

'''

str = "HelloWorld!"
str = str.center(10)
print(str)

'''

'''

str = "the Story of Interest"
print(str.title())

'''

'''

hello = {"Data Structor": "数据结构", 'Database': '数据库'}
print(hello.items())

'''

'''

hello = {"Google", "Runoob", "Taobao"}
hello.clear()
print(hello)

'''

'''

age = int(input("请输入你家狗狗的年龄："))
print("")
if age <= 0:
    print("Are you kidding me?")
elif age == 1:
    print("About 14 years old of human beings.")
elif age > 2:
    human = 22 + (age - 2) * 5
    print(f"About {human} years old of human.")

'''

'''

subject = 2
match subject:
    case 1:
        print("This is one!")
    case 2:
        print("Aha!")
    case 3:
        print("Hello, this world!")
    case _:
        print("What are you saying, yet?")
# 这里不像传统的 switch-case 结构，直接每一个分支都阻塞

'''

'''

a, b, n = 0, 1, 10
for i in range(n):
    print(f"{a}, {b}")
    a, b = b, a + b
# 表达式 a, b = b, a + b
# 会在赋值之前先计算右边的式子（右边式子按照从左往右的顺序），然后再执行赋值操作

'''

'''

b = {x for x in 'abcdesfs'}
print(b)
print(set(b))
print("*"*30)
a = (x for x in range(1, 10))
print(a)
print(tuple(a))
# 元组与其他 python 数据类型不同的一点

'''

'''

from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("h1"):
    print("这是一个标题")

'''

'''

class Timer:
    def _enter_(self):
        import time
        self.start = time.time()
        return self
    def _exit_(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        print(f"耗时：{self.end - self.start:.2f}秒")
        return False

with Timer() as t:
    sum(range(1000000))

'''

'''

def change(a):
    print(f"函数内 a 的地址：{id(a)}")
    a = 10
    print(f"函数内修改 a 的值之后 a 的地址：{id(a)}")

a = 1
print(f"主程序中 a 的地址：{id(a)}")
change(a)
print(a)

'''

# 牛马关键字参数
def printinfo(name, age):
    print("名字：", name)
    print("年龄：", age)
    return 

printinfo(age = 50, name = "runoob")








