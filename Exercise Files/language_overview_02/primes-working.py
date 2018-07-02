#!/usr/bin/env python3

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n %i == 0:
                return False
        return True

def list_prime():
    for n in range(100):
        if is_prime(n):
            print(n, end=' ', flush=True)
    print()

list_prime()

