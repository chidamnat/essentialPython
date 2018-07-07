#!/usr/bin/env python3

def main():
    infile = open('lines.txt','rt')           # open a file in read mode in text format
    outfile = open('lines-copy.txt','wt')     # open a file in write mode in text format
    for line in infile:
        # print(line.rstrip(), file = outfile)    # Advantage of this is line endings are handled across the Operating systems
        outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close()
    infile.close()
    print('\n done.')

if __name__ == '__main__':
    main()