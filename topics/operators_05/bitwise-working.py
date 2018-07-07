#!/usr/bin/env

x = 0x0a
y = 0x02
z = x & y
xor = x ^ y

print("(hex) x is {0:02x}, y is {1:02x}, z is {2:02x}".format(x, y, z))
print("(bin) x is {0:08b}, y is {1:08b}, z is {2:08b}".format(x, y , z))

print("(bin) x is {0:08b}, y is {1:08b}, xor(x, y) is {2:08b}".format(x, y , xor))