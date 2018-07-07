#!/usr/bin/env python3

#kwargs or keyword argguments works like a dictionary are positional arguments
def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    print()
    x = dict(Johnny = 'woof', Tikki = 'boof', White = 'hoof')
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print("kitten {} says {} ".format(k, kwargs[k]))
    else:
        print("Meow.")

if __name__ == '__main__':
    main()