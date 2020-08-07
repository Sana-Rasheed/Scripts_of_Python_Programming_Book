# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:51:01 2020

@author: sana.rasheed
"""
### Chapter 9th - Inheritance 

# Example 15
# Fruit class defined as parent
class Fruit:
    """
    A class is defined for fruits,
    to create objects of this class..
    """
    def __init__(self, name, nutrients):
        try:
            assert type(nutrients) == list
        except AssertionError:
            print('invalid construction')
            raise Exception
        self.name = name
        self.nutrients = nutrients
        self.is_ripe = False
    def get_name(self):
        return self.name
    def get_nutrients (self):
      print(self.name + ' has following nutrients:')
      for value in self.nutrients:
          print (value)
    def check_ripeness(self):
      return self.is_ripe
    def ripe_fruit(self):
      self.is_ripe = True
# End of Fruit class 

# Citrus is an Inherited Class of Fruit
class Citrus(Fruit):
        def __init__(self, name, nutrients):
             super().__init__( name,nutrients)
             self.type= 'Citrus'
             self.characteristic = 'Pulpy and Juicy'
        def get_type(self):
            return self.type
# End of Citrus class 

Orange = Citrus(name='Orange', nutrients=['vitamin D','vitamin C'])   
Orange.get_nutrients()  

# Output
# Orange has following nutrients:
# vitamin D
# vitamin C
