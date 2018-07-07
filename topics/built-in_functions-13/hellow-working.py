#!/usr/bin/env python3

class Bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return "repr: The number of bunnies is {}".format(self._n)
    
    def __str__(self):
        return "str: The number of bunnies is {}".format(self._n)


x = Bunny(42)
print(x)
print(repr(x))
print()

y = (0, 1, 2, 3, 4, 5)
z = reversed(y)        # returns an iterator
print(y)
print(z)
for i in z:
    print(i, end = ' ')
print("\n sum = {}".format(sum(y)))
print(" sum with 10 as initial value {}".format(sum(y, 10)))    # sum function wurg a starting value

print(" minimum value of y: {}".format(min(y)))
print(" maximum value of y: {}".format(max(y)))
print(" any(y): {}".format(any(y)))   # if any of this is True
print(" all(y): {}".format(all(y)))   # if all of this is True
v = (6,7,8,9,10,11)
a = zip(y,v)   # returns an iterator
for i,j in a:
    print("{},{}".format(i,j))
print()

x = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, name in enumerate(x):
    print("{} - {}".format(i, name))
print()
