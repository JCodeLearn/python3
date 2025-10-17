#! /usr/bin/env python3

'''

with open("./test.txt", 'w') as book:
    book.write("Python 是一个非常好的解释型语言。\nYes, it's really good！\n")

'''

'''

with open("./test.txt", 'r') as book:
    for line in book:
        print(line, end='')

'''
with open('./foo.txt', 'w') as x:
    pass

with open('./foo.txt', 'rb+') as f:
    f.write(b'0123456789abcdef')
    f.seek(5)
    print(f.read(1))
    f.seek(-3, 2)
    print(f.read(1))

