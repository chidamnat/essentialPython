#!/usr/bin/env python3

x = 10
y = 20
data = ('bear', 'tiger', 'lion', 'mouse', 'fox')
inp = 'bear'

if inp in data:
    print("expression is True")
else:
    print("expression is False")

if inp is data[0]:
    print("Expression is True")
else:
    print("Expression is False")

print(id(inp))
print(id(data[0]))