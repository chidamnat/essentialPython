#!/usr/bin/env python3

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0 
        self._step = 1

        # argument validation
        if numargs < 1:
            raise TypeError("expected at least 1 argument, but got {}".format(numargs))
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError("expected at most 3 arguments, but got {}".format(numargs))
        
        self._next = self._start

    def __iter__(self):
        return self

    def __next__(self):
        if self._next > self._stop:
            raise StopIteration
        else:
            _r = self._next
            self._next += self._step
            return _r

def main():
    for n in inclusive_range(25):
        print(n, end = " ")
    print()

    for n in inclusive_range(1, 100, 3):
        print(n, end = ' ')
    print()

    for n in inclusive_range(10):
        print(n, end = ' ')
    print()

if __name__ == '__main__':
    main()