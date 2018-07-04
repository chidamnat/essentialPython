#!/usr/bin/env python3

def main():
    for i in range(25):
        print(i, end = ' ')
    print()

    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    start, step = 0, 1
    numargs = len(args)

    # initialize parameters
    if numargs < 1:
        raise TypeError("expected at least 1 argument, got {}".format(numargs))
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("expected at most 3 arguments, got {}".format(args))

    #generator
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__':
    main()