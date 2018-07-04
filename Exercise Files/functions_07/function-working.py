#!/usr/bin/env python3

def main():
    x = 5
    kitten(x)  #Python uses call by value but still the side effects on integer not reflected as it is immutable
    print("x = {}".format(x))

    x = [5]
    kitten1(x) # Now python uses a mutable List to allow sideeffect to happen!
    print("Now x = {}".format(x))

def kitten(a):
    a = 3
    print("Meow and a = {} ".format(a))

def kitten1(a):
    a[0] = 3
    print("Meow and x = {}".format(a))

if __name__ == '__main__':
    main()