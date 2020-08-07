# import libraries
import logging
import time
import datetime 
import threading 

def get_cubic(num): 
     print(datetime.datetime.now())
     print("Cube: {}".format(num * num * num)) 

def get_inverse(num):
     print(datetime.datetime.now())
     print("Inverted: {}".format(1 / num)) 

# Example 1
# main  execution
if __name__ == "__main__": 
     # creating thread 
     t1 = threading.Thread(target=get_cubic, args=(10,)) 
     t2 = threading.Thread(target=get_inverse, args=(10,)) 
     # Starting the threads 
     t1.start() 
     t2.start()
     # waiting for each to finish  
     t1.join() 
     t2.join() 
     # both threads completely executed 
     print("Done!") 

# Output
# Cube: 1000  
# Inverted: 0.1
# Done!


# Example 2
if __name__ == "__main__":
    # creating thread 
     t1 = threading.Thread(target=get_cubic, args=(10,)) 
     t2 = threading.Thread(target=get_inverse, args=('10',)) 
     # Starting the threads 
     t1.start() 
     t2.start()
     # waiting for each to finish  
     t1.join() 
     t2.join() 
     # both threads completely executed 
     print("Done!") 


# Output

# Cube: 1000
# Done!
# Exception in thread Thread-16:
# Traceback (most recent call last):
#   File "C:\Users\anaconda3\lib\threading.py", line 926, in _bootstrap_inner
#    self.run()
#   File "C:\Users\anaconda3\lib\threading.py", line 870, in run
#    self._target(*self._args, **self._kwargs)
#   File "E:\Python task\Python\4.8.Threading.py", line 12, in get_inverse         
#   print("Inverted: {}".format(1 / num))
# TypeError: unsupported operand type(s) for /: 'int' and 'str'  
