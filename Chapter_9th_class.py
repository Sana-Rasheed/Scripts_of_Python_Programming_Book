# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:15:35 2020

@author: sana.rasheed
"""

### Chapter 9th - Class

# Example 1
class MyClass:
	x = 5
print(MyClass)

# Output
# <class '__main__.MyClass'>


# Example 2
class MyClass:
	x = 5

p1 = MyClass()
print(p1.x)

# Output
# 5


# Example 3
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# Output
# John
# 36


# Example 4
class Person:
	def __init__(myobject, name, age):
		myobject.name = name
		myobject.age = age
	def myfunc(abc):
		print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Output
# Hello my name is John


# Example 5
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

# Output
# Hello my name is John



# Example 6
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)

# Output
# 40


# Example 7
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age # delete p1.age
print(p1.age) # return an error as p1.age is deleted

# Output
# AttributeError: 'Person' object has no attribute 'age'


# Example 8
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def myfunc(self):
		print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1 # delete p1
print(p1)  # return an error as p1 is deleted

# Output
# NameError: name 'p1' is not defined

