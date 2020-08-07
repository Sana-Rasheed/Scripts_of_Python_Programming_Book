# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:26:42 2020

@author: sana.rasheed
"""
# Chapter 17th 
# Example 4
import cProfile
def  internal_method():
    temp_var = 0
    for ind in range(10000):
        temp_var += 1
    return temp_var

def  external_method():
    counter = 0
    for val in range(10):
        counter += internal_method()
    print('Total iterations:', counter)
    return 

cProfile.run('external_method()')

# Output
# Total iterations: 100000
# 75 function calls in 0.015 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime    percall filename:lineno(function)
# 10    0.014    0.001     0.014        0.001 8. profiling.py:3(internal_method)
# 1    0.000     0.000     0.015      0.015 8. profiling.py:9(external_method)
# 1    0.000     0.000     0.015       0.015 <string>:1(<module>)
# 5    0.000     0.000     0.001       0.000 iostream.py:197(schedule)                                  
# 4    0.000     0.000     0.000       0.000 iostream.py:309(_is_master_process)
# 4    0.000     0.000     0.000        0.000 iostream.py:322(_schedule_flush)
# 4    0.000     0.000     0.001       0.000 iostream.py:384(write)
# 5    0.000     0.000     0.000        0.000 iostream.py:93(_event_pipe)
# 5    0.001    0.000    0.001    0.000 socket.py:342(send)
# 5    0.000    0.000    0.000    0.000 threading.py:1050(_wait_for_tstate_lock)
# 5    0.000    0.000    0.000    0.000 threading.py:1092(is_alive)
# 5    0.000    0.000    0.000    0.000 threading.py:507(is_set)
# 1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
# 4    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
# 1    0.000    0.000    0.001    0.001 {built-in method builtins.print}
# 4    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
# 5    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.lock' objects}
# 5    0.000    0.000    0.000    0.000 {method 'append' of 'collections.deque' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
