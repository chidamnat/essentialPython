#!/usr/bin/env python3

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    ## some important list slicing
    i = game.index('Paper')  # finding the location of a particular item in the list
    print(i, game[i]) # printing a particular position of the list
    print(game[1:4:2]) # printing the list with start, end and step size
    print(game[::-1]) # reversing the list
    game.insert(0, "Computer") # to insert an item in a particular position of a list
    x = game.pop()  # to remove an itenm from the end of the list
    print("removed item from the list is: {}".format(x))
    game.pop(3) # pop is also used to remove an item from a particular index
    # del game[3]  # is the same as pop but won't return the value as pop did
    print_list(game) 
    del game[1:5:2]
    print()
    print_list(game) 
    print(','.join(game)) # join a list using a delimiter

def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()

if __name__ == '__main__':
    main()