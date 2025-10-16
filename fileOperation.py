#! /usr/bin/env python3

with open("./test.txt", 'w') as book:
    book.write("Python 是一个非常好的解释型语言。\nYes, it's really good！\n")

with open("./test.txt", 'r') as book:
    for line in book:
        print(line, end='')