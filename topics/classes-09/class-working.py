#!/usr/bin/env python3

class Duck:
    sound = "Quack quack."
    movement = "Walks like a duck."

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)
    
donald = Duck()
donald.quack()
donald.move()