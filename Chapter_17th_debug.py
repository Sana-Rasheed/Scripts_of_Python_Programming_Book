# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:27:32 2020

@author: sana.rasheed
"""
# Chapter 17th 
# Example 3
import pdb
def  sum_values(a, b):
    return a + b

def test_function():
    pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.     
    print('This is the first line')
    print("This is the second line.")
    value  = sum_values(2, 3)
    print('The code is done!')
    return value    

#  execute the function
test_function()

# Output
# > e:\task\python task\python\python\3. debugging.py(8)test_function()
#       6 def test_function():
#       7     pdb.set_trace()  #we have added a breakpoint here. The code pause execution here.
# ----> 8     print('This is the first line')
#       9     print("This is the second line.")
#      10     value  = sum_values(2, 3)


