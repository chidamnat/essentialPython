#!/usr/bin/env python3

x = [1, 2, 3, 4, 5]
x[2] = 42  # List is mutable
for i in x:
    print('i is {}'.format(i))
print()

x = (1, 2, 3, 4, 5)
#x[4] = 42          # Tuple is immutable
for i in x:
    print('i is {}'.format(i))
print()

x = range(10)
# x[2] = 42                            # Like tuple, range is also immutable
# x = range(5, 10)                     # other variations in range
# x = range(5, 50, 5)
for i in x:
    print('i is {}'.format(i))
print()

x = {'one': 1, 'two': 2, 'three': 3, 'four':4, 'five':5 }
x[3] = 42      # dictionaries are mutable!
for k, v in x.items():
    print('k: {} and v: {}'.format(k,v))

