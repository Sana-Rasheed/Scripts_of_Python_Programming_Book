# Example 1
print('Hello')
print("Hello")

# Output
# Hello
# Hello


# Example  2
a = "Hello"
print(a)


# Example 3
# Creating a multiline string
a = """I'm learning Python.
I refer to TechBeamers.com tutorials.
It is the most popular site for Python programmers."""
print(a)


# Example 4
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

# Example 5
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Example 6
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# Example 7
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Example 8
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Example 9
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Output
# banana


# Example 10
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Output
# cherry


# Example 11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Output
# ['cherry', 'orange', 'kiwi']

# Example 12
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Output
# banana


# Example 13
thisdict ={
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964 
	}
print(thisdict)

# Output
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# Example 14
thisdict ={
	"brand": "Ford",
	"model": "Mustang",
	"year": 1964 
	}
x = thisdict["model"] 
print(x)

# Output 
# Mustang


# Example 15
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Output
# {'apple', 'cherry', 'banana'}


# Example 16
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Output 
# {'apple', 'cherry', 'orange', 'banana'}

# Example 17
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

# Output
# {'orange', 'cherry', 'banana', 'apple', 'mango', 'grapes'}


# Example 18
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Output
# 3


# Example 19
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Output
# {'apple','cherry'}

# Example 20
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")
print(cities)

# Output
# Traceback (most recent call last):
#   File "C:\Users\.spyder-py3\temp.py", line 2, in <module>
#     cities.add("Strasbourg")
# AttributeError: 'frozenset' object has no attribute 'add'


# Example 21
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Output
# True
# False
# False


# Example 22
a = 200
b = 33
if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")

# Output
# b is not greater than a



# Example 23
# create a str
x = b'Python mapping table characters'
print(x)

# Output
# b'Python mapping table characters'


# Example 24
x = b"Bytes objects are immutable sequences of single bytes"
print(x)

# Output
# b'Bytes objects are immutable sequences of single bytes'


# Example 25
# triple single or double quotes allows multiple lines
x = b'''Python Tutorial,
Javascript Tutorial,
MySQL Tutorial'''
print(x)

# Output
# b'Python Tutorial,\nJavascript Tutorial,\nMySQL Tutorial'



# Example 26
string = "Python is interesting."
# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

# Output
# bytearray(b'Python is interesting.')


# Example 27
import datetime 
x = datetime.datetime.now() 
print(x)

# Output
# 2020-07-03 17:37:07.999021


# Example 28
import datetime 
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Output
# 2020 
# Friday


# Example 29
import datetime
x = datetime.datetime.now() # current date and time
year = x.strftime("%Y")
month = x.strftime("%m")
day = x.strftime("%d")
print("day: ", day)
time = x.strftime("%H:%M:%S")
print("time: ", time)
date_time = x.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:", date_time)

# Output
# day:  03
# time:  13:25:36
# date and time: 07/03/2020, 13:25:36


# Example 30
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
s1 = now.strftime("%m/%d/%Y") # mm/dd/YY format
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y") # dd/mm/YY  format
print("s2:", s2)
s3 = now.strftime("%d-%m-%Y") # dd-mm-YY  format
print("s3:", s3)
s4 = now.strftime("%a-%b-%y")  
print("s4:", s4)
s5 = now.strftime("%A-%B-%Y")
print("s5:", s5)


# Output
# time: 13:42:48
# s1: 07/16/2020
# s2: 16/07/2020 
# s3: 16-07-2020 
# s4: Thu-Jul-20  
# s5: Thursday-July-2020

