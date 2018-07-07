#!/usr/bin/env python3

def main():
    a = set("we are gonna need a bigger boat.")
    b = set(" I am sorry Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    print_set(a & b)  # set intersection
    print_set(a | b)  # set union
    print_set(a ^ b)  # set xor 

def print_set(o):
    print('{', end = '')
    for x in o:
        print(x, end = '')
    print('}')

if __name__ == '__main__':
    main()