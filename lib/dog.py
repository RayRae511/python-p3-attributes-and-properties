#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        self._name = None
    def name(self):
        return self._name
    def name(self, val):
        if name(val, str) and 1 <= len(val) <= 25:
            self._name = val
        else:
            print("Name must be string between 1 and 25 characters")
    def breed(self):
        return self._breed
    def breed(self, val):
        if val in APPROVED_BREEDS:
            self._breed = val
        else:
            print("Breed must be in list of approved breeds")
    pass

doggo = Dog()
doggo.name = "Rex"
doggo.breed = "Chihuahua"
# Output: Breed must be in list of approved breeds.