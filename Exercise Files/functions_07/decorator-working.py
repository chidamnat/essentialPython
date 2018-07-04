#!/usr/bin/env python3

def f1(f):
    def f2():
        print("this is before the function call")
        f()
        print("this is after the function call")
    return f2

def f3():
    print("This is f3")


wrapper_for_f3 = f1(f3)
wrapper_for_f3()
print()

# There is a easy way to do.. use decorators!!
@f1
def f4():
    print("This is f4")

f4()