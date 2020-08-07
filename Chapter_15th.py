
# Example 1
class Greeter: 
    def _init_(self, name):
        self.name= _name      
    def say_hello(self):
        print('hello {}!'.format(self.name))      
    def say_goodbye(self):
        print('goodbye {}!'.format(self.name))
# End of class

my_greeter= Greeter()
print('get id,type and available methods and attributes for Greeter class:')
print(id(my_greeter))
print(type(my_greeter))
print(dir(my_greeter))

# Output
# get id,type and available methods and attributes for Greeter class: 2387805337096
# <class '__main__.Greeter'>
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_init_', 'say_goodbye', 'say_hello']



# Example 2
my_var= 'This is a variable'
print('\ncheck id,type and methods for a variable containing string value:')
print(id(my_var))
print(type(my_var))
print(dir(my_var))

# Output
# check id,type and methods for a variable containing string value: 2387807488400
# <class 'str'> 
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



# Example 3
my_num=453.324
print('\ncheck id,type and methods for a variable containing numeric value:')
print(id(my_num))
print(type(my_num))
print(dir(my_num))

# Output
# check id,type and methods for a variable containing numeric value: 2387807736720
# <class 'float'>
# ['__abs__', '__add__', '__bool__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']



# Example 4
import inspect # imported inspect module
import os
testvar= 'Hello'
class Greeter:
    def _init_(self,name):
        self.name= name
    def say_hello(self):
        print('Hello {}!'.format(self.name))
    def say_goodbye(self):
        print('Goodbye {}!'.format(self.name))
# End of class

my_greeter= Greeter() # class object

#lambda function
exp = lambda x:x*x

# normal python user-definedfunction/method
def show_name_age(first_name:str,last_name:str,age:int):
    print('{} {} is {} years old'.format(first_name,last_name,age))

inspect.getmembers(my_greeter) # returns members of the class my_greeter   
# print( inspect.getmembers(my_greeter) )

# introspection of ismodule 
print('\n Checking if os is a module:', inspect.ismodule(os)) 
print('\n Checking if testvar is a module:', inspect.ismodule(testvar))
print('\n Inspect ismethod vs. isfunction comparison'.upper())

# introspection of is method
print('\n Ismethod:\n show_name_age:', inspect.ismethod(show_name_age), 
		'exp:', inspect.ismethod(exp), 
		'Greeter.say_hello:', inspect.ismethod(my_greeter.say_hello) )  

# introspection of is function
print('\n Isfunction:\n show_name_age:',inspect.isfunction(show_name_age), 
		'exp:', inspect.isfunction(exp),
		'Greeter.say_hello:', inspect.isfunction(my_greeter.say_hello) )


# Output
# Checking if os is a module: True
# Checking if testvar is a module: False
# INSPECT ISMETHOD VS. ISFUNCTION COMPARISON                           
# Ismethod:
# show_name_age: False  exp: False  Greeter.say_hello: True
# Isfunction:
# show_name_age: True  exp: True  Greeter.say_hello: False




# Example 5
import inspect
# normal python user-defined function/method
def  show_name_age(first_name:str,last_name:str,age:int):
    print('{} {} is {} years old'.format(first_name,last_name,age))

#signature of a method:accesses parameters,their inferred or fixed data types.
sig= inspect.signature(show_name_age)
print (sig.parameters) 

# Output 
# OrderedDict([('first_name', <Parameter "first_name: str">), ('last_name', <Parameter "last_name: str">),
#  ('age', <Parameter "age: int">)])      


# Example 6
print(sig.parameters['first_name'].annotation)

# Output
# <class 'str'>


### Decorator 
print("\n\nDecorator Example")
# Example 7
def extract_function_name(func): 
     def internal_method(*args, **kwargs): 
         print('The method called is:', func.__name__)
         returned_value = func(*args, **kwargs)
         print('The method execution is complete.')
         return returned_value 
     return internal_method
  
# adding decorator to the function 
@extract_function_name
def sum_two_numbers(a, b): 
    print("This is called inside the function") 
    return a + b 

@extract_function_name
def product_two_numbers(a, b): 
    print("This is called inside the function") 
    return a*b 

a, b = 3, 4
# getting the value through return of the function 
print('Sum function value:', sum_two_numbers(a, b))
print('Product function value', product_two_numbers(a, b))

# Output 
# The method called is: sum_two_numbers
# This is called inside the function
# The method execution is complete.
# Sum function value: 7 
# The method called is: product_two_numbers
# This is called inside the function
# The method execution is complete.
# Product function value 12



