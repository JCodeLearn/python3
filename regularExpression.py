#! /usr/bin/env python3
import re

# test1
"""

pattern = r"<([a-z][a-z0-9]*)\b[^>]*>.*?</\1>"
string = r"<font>set character color</font>"
print(re.search(pattern, string, flags=0))

"""

# test2

pattern = r"\b(\w+)\b\s+\1\b"
string = "hello hello hello hello hello"
print(re.findall(pattern, string))
