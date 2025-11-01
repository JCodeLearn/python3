#! /usr/bin/env python3
import re

# test1
"""

pattern = r"<([a-z][a-z0-9]*)\b[^>]*>.*?</\1>"
string = r"<font>set character color</font>"
print(re.search(pattern, string, flags=0))

"""

# test2

"""

pattern = r"\b(\w+)\b\s+\1\b"
string = "hello hello hello hello hello"
print(re.findall(pattern, string))
print(type(re.match(pattern, string)))

"""

# test3

"""

pattern = re.compile(r'\d+')
# print(pattern.search('one12twothree34four').group())
string = 'one12twothree34four'
print(type(re.findall(pattern, string)))


"""

# test4

"""

pattern = r"(\d+)"
string = 'one12twothree34four'
print(re.compile(pattern).findall(string))


"""

# test5

"""

pattern = r"\d+"
string = 'one12twothree34four'
it = re.compile(pattern).finditer(string)
for match in it:
    print(match.group())

"""

# test6

"""

phone = "2004-959-999 # 这是一个电话号码"
num = re.sub(r'#.*$', "", phone) 
print(num)

"""

# test7 
"""

def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

s = 'A23G3HFD567'
print(re.sub('(?P<value>\d+)', double, s))

"""

# print(type(re.compile(r"/w+")))
