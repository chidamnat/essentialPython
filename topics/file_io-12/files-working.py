#!/usr/bin/env python3

def main():
    f = open('lines.txt','r')    # default mode is read
    for line in f:
        print(line.rstrip())    # strips any new lines or whitepaces towards the end

if __name__ == '__main__':
    main()