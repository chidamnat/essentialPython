#!/usr/bin/env python3

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    if numargs < 1:
        raise TypeError("expected at least 1 argument, but gor {}".format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("Expected at most 3 arguments, but got {}".format(numargs))
    
    # generator
    i = start
    while i <= stop:
        yield i
        i += step
    
def main():
    try:
        for n in inclusive_range(25):
            print(n, end = ' ')
        print()

        for n in inclusive_range(1,10,2,3):
            print(n, end = ' ')
        print()
    except TypeError as e:
        print("range error: {}".format(e))

if __name__ == '__main__':
    main()
    