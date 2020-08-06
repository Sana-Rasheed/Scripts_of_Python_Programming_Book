# Example 1
def my_function():
	print("Hello from a function")
my_function()

# Output
# Hello from a function


# Example 2
def my_function(fname):
	print(fname + " Robert")

my_function("Emily")
my_function("John")
my_function("Julia")

# Output
# Emily Robert
# John Robert
# Julia Robert


# Example 3
def my_function(fname, lname):
	print(fname + " " + lname)

my_function("Emily", "Robert")

# Output
# Emily Robert


# Example 4
def my_function(fname, lname):
	print(fname + " " + lname)

my_function("Emily")

# Output
# TypeError:  my_function() missing 1 required positional argument: 'lname'


# Example 5
def my_function(country = "Norway"):
	print("I am from " + country)

my_function("Pakistan")
my_function("Sweden")
my_function()
my_function("China")

# Output
# I am from Pakistan 
# I am from Sweden  
# I am from Norway  
# I am from China


# Example 6
def my_function(*kids):
	print("The youngest child is " + kids[2])

my_function("Emily", "John", "Julia")

# Output
# The youngest child is Julia


# Example 7
def my_function(child3, child2, child1):
	print("The youngest child is " + child3)

my_function(child1 = "Emily", child2 = "John", child3 = "Julia")

# Output
# The youngest child is Julia


# Example 8
def my_function(child3, child2, child1):
	print("The youngest child is " + child3)

my_function(child3 = "Julia", child2 = "John",child1 = "Emily" )


# Output
# The youngest child is Julia


# Example 9
def my_function(**kid):
	print("His last name is " + kid["lname"])

my_function(fname = "John", lname = "Robert")

# Output
# His last name is Robert


# Example  10
def my_function(food):
	for x in food:
		print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Output
# apple
# banana
# cherry


# Example 11
def my_function(x):
	return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# Output
# 15
# 25
# 45


# Example 12
def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# Output
# Recursion Example Results
# 1
# 3
# 6
# 10
# 15
# 21

# Example 13
x = lambda a: a + 10
print(x(5))

# Output
# 15

# Example 14
x = lambda a, b: a * b 
print(x(5, 6))

# Output 
# 30


# Example 15
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# Output
# 13 


# Example 16
def  myfunc(n):
	return lambda a : a * n

mydoubler = myfunc(2) 
print(mydoubler(11))

# Output 
# 22 

mytripler = myfunc(3)
print(mytripler(11))

# Output 
# 33

mydoubler = myfunc(2) 
mytripler = myfunc(3)  
print(mydoubler(11))  
print(mytripler(11))

# Output
# 22
# 33
