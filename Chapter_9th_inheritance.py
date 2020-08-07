# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:15:35 2020

@author: sana.rasheed
"""

### Chapter 9th - Inheritance 
'''
Author Note:
    For the sake of learning, I have redefined parent class for each example, 
    so you execute it successfully. However, we define classes only ONE TIME.
'''
# Example 9
class Person:
   def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname
   def printname(self):
      print(self.firstname, self.lastname)

x = Person("John", "Robert")
x.printname()

# Output
# John Robert


# Example 10 
class Person:
   def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname
   def printname(self):
      print(self.firstname, self.lastname)

class Student(Person):
   pass

x = Student("Mike", "Olsen")
x.printname()

# Output
# Mike Olsen


# Example 11
class Person:
   def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname
   def printname(self):
      print(self.firstname, self.lastname)

class Student(Person):
   def __init__(self, fname, lname):
      Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# Output
# Mike Olsen


# Example 12
class Person:
   def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname
   def printname(self):
      print(self.firstname, self.lastname)

class Student(Person):
   def __init__(self, fname, lname):
      super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

# Output
# Mike Olsen


# Example 13
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2020

x = Student("Olivia", "Brown")
print(x.graduationyear)

# Output 
# 2020



# Example 14

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Olivia", "Brown", 2020)
x.welcome()

# Output
# Welcome Olivia Brown to the class of 2020


