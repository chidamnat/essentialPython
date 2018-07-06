#!/usr/bin/env python3

import sys

def main():
    try:
        # x = int("foo")
        y = 10/0
    except ValueError:
        print("Caught a ValueError")
    # except ZeroDivisionError:
    #     print("don't divide by zero")
    except:
        # print("Unknown error: {}".format(sys.exc_info()))
        print("Unknown error: {}".format(sys.exc_info()[1]))
    else:
        print('good job!')
        print(y)

if __name__ == '__main__':
    main()
