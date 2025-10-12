#! /usr/bin/env python3

import time

for i in range(101):
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end = '', flush = True)
    time.sleep(0.05)
print()