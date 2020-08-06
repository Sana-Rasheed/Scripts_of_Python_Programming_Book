# Example 
# 3/0 # type it directly in terminal - it will give you following error
# Traceback (most recent call last):
# 	File "<ipython-input-31-f6cc6d14333b>", line 1, in <module>
# 		3/0
# 	ZeroDivisionError: division by zero


# Example 
divisor = 0  
try:
	value = 22/divisor 
except ZeroDivisionError:  
	print('The divisor provided was zero.')


# Example 
my_numbers=[1,2,3,4]
print('The length of the list is:', len(my_numbers))
#my_numbers[4] # this will give you an error

# Output: 
# The length of this list is: 4  
# IndexError: list index out of range


# Example 
try:
    my_numbers[4]
except IndexError:
    print('The index you used is invalid.')

print('The code executed.')

# Output:
# The index you used is invalid.
# The code executed.


# Example 
def check_type(year):
    assert type(year) == int, 'The type of year is not integer'
    print('The type of year is valid.')
    return True

check_type(year=2010) # The type of year is valid.

# Example this will give you error after uncomment
# check_type(year=2010.22) # AssertionError: The type of year is not integer.


# Example 
def check_type(year):
    try:
        assert type(year) == int
    except AssertionError:
        print('The type of year is invalid')
        return False
    return True

print(check_type(year=2010.22)) 
# The type of year is invalid. 
# False 
print(check_type(year=2010))
# True 


# Example 
try:
    print(x)
except: 
	print("An exception occurred")

# Output
# An exception occurred


# Example 
try:
	print(x)
except: 
	print("Something went wrong")
finally:
	print("The 'try except' is finished")

# Output
# Something went wrong 
# The 'try except' is finished

