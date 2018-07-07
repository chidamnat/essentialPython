#!/usr/bin/env python3 

import sys  # import the module
import os
import random
import datetime

def main():
    # sys module
    v = sys.version_info   # accessing an element of the class in the module
    print('Python version {}.{}.{}'.format(*v))   # major.minor.micro version

    v = sys.platform
    print('Python platform {}'.format(v))

    # os module
    v = os.name
    print("os name = {}".format(v))

    v = os.getenv('PATH')
    print('os getenv: {}'.format(v))

    v = os.getcwd()
    print('os getcwd: {}'.format(v))

    v = os.urandom(25).hex()
    print("os urandom: {}".format(v))

    # random module
    x = random.randint(1, 1000)
    print(' random.randint between 1 and 1000 : {}'.format(x))

    x = list(range(25))     # formed a list of the iterator
    print('x = {}'.format(x))
    random.shuffle(x)  # affects in place
    print ('shuffled x = {}'.format(x))

    # datetime module
    now = datetime.datetime.now()
    print("now = {}".format(now))
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__':
    main()