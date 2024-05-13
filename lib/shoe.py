#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size=0, condition="used"):
        self._size = size
        self._brand = brand
        self._condition = condition

    @property
    def brand(self):
        """This is the brand property"""
        return self._brand
    
    @property
    def size(self):
        """This is the size property"""
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self.size = size
        else: 
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")

    condition = "New"