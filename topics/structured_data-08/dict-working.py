#!/usr/bin/env python3

def main():
    animals = {'kitten': 'meow', 'lion': 'roar', 'puppy': 'ruff!', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)
    print()
    # dictionaries can be created by dict constructor
    animal_dict = dict(kitten = 'meow', lion = 'roar', puppy = 'ruff!', giraffe = 'I am a giraffe!', dragon = 'rawr')
    print_dict(animal_dict)
    print()
    # Another way to print the dictionary using the for loop
    for k,v in animal_dict.items():
        print(k , ":" , v)
    print()
    # printing only the keys of a dictionary
    for k in animal_dict.keys():
        print(k)
    print()
    # printing only the values of a dictionary
    for v in animal_dict.values():
        print(v)
    print()
    # printing particular element in a dictionary
    print(animal_dict['lion'])
    print()
    # Adding a new item
    animal_dict['Monkey'] = "haha"
    print(animal_dict)
    print()
    # search for an animal! / item using in operator
    print("is Monkey in the dictionary:", str("Monkey" in animal_dict))
    # whenevr using the conditional expression we need both if and else part as shown below
    print('found!' if 'lion' in animals else "not found!")
    # to avoid KeyEror use get on the dictionary
    print(animals.get('godzilla'))


def print_dict(o):
    for x in o:
        print(" {}: {}".format(x, o[x]))

if __name__ == '__main__':
    main()