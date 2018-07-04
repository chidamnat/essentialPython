#!/usr/bin/env python3

#list arguments
def main():
    kitten('meow','grrr','purr')
    print()
    x = ('woof','wag','dag')
    kitten(*x)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("Meow")

if __name__ == '__main__':
    main()