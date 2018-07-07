#!/usr/bin/env python3

x = 7
print("x = {}".format(x))
print(type(x))

y = 'sample'.capitalize()
print("y capitalize = " + y)
print("y upper = " + 'sample'.upper())
print(type(y))

x = 'seven {1} {0}'.format(8,9)    # These are positional arguments
print("x = " + x)

x = 'seven {1:<9} {0:>9}'.format(8,9) # left justified and right justified
print("x = " + x)

x = 'seven "{1:<09} {0:>09}"'.format(8,9) # zeros filled
print("x = " + x)

a, b = 9, 8
# x = f'seven {a} {b}'        # fstring is available from python 3.6 onwards
# print("x = " + x)


x = 7 / 3
y = 7 // 3
print('x is {}'.format(x))
print(type(x))    # This is a float
print('y is {}'.format(y))
print(type(y))    # This is an int

x = 0.1 + 0.1 + 0.1 - 0.3
print('x is {}'.format(x))   # surprisingly the answer is not 0
print(type(x))
""" So generally avoid using floating point number for storing money!!"""
# This is how we solve this problem

from decimal import Decimal 
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))  #Now it will balance your books nicely!!
print(type(x))


x = False
print('x is {}'.format(x))
print(type(x))

x = None
print('x is {}'.format(x))
print(type(x))

if x:
    print('True')
else:
    print('False')    # This evaluates to False 

x = (1, 2, 3, 4, 5)
print('x is {}'.format(x))
print(type(x))

x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(type(x[1]))
print(type(y))

print(id(x))   # Though x and y have same values yet they are stored as 2 different objects
print(id(y))
if x is y:
    print("Yep")
else:
    print("nope")

print(id(x[0]))    # surprisingly the id of subelement is same!
print(id(y[0]))

if x[0] is y[0]:
    print("yep")
else:
    print("nope")

if isinstance(x, tuple):
    print('tuple')
elif isinstance(x, list):
    print("list")
else:
    print('nope')
     