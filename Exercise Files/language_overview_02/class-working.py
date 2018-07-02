#!/usr/bin/env python3

class Duck:
    sound = "Quaaaack"
    walking = "waalk like a duck"

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.walk()
    donald.quack()

if __name__ == '__main__':
    main()