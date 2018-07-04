#!/usr/bin/env python3

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]   # each element multiplied by 2
    seq3 = [x for x in seq if x % 3 != 0 ]   # elements that are not divisible by 3
    seq4 = [ (x, x*x) for x in seq ] # tuple of element and its square 
    
    from math import pi
    seq5 = [round(pi, i) for i in seq] # rounding pi!
    seq6 = { x: x**2 for x in seq } # creating a dictionary!
    seq7 = { x for x in "superduper" if x not in 'pd' } # creating a set
    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)

def print_list(o):
    for x in o: print(x, end = '  ')
    print()

if __name__ == '__main__':
    main()