# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:54:29 2020

@author: sana.rasheed
"""

# Example 1
import subprocess
# run the command
subprocess.call(['dir'], shell= True) # returns the files in the current directory

# Output
# 0


# Exammple 2
import subprocess # import module
# run the command
output =subprocess.check_output(['dir'], shell= True) # returns the files in the current directory
print(output)

# Output
# b' Volume in drive E is New Volume\r\n Volume Serial Number is 100E-A8F7\r\n\r\n Directory of E:\\task\\Python task\\Python\\Python\r\n\r\n08/07/2020  03:57 pm    <DIR>          .\r\n08/07/2020  03:57 pm    <DIR>          ..\r\n06/07/2020  05:10 pm               611 2. testing.py\r\n07/07/2020  07:20 am               345 3. debugging.py\r\n11/06/2020  03:04 pm             1,849 4.10.numpy.py\r\n11/06/2020  03:04 pm               833 4.10.numpy_linear_algebra.py\r\n11/06/2020  03:04 pm               906 4.4.lxml.py\r\n08/07/2020  03:57 pm             1,311 4.6.configparser.py\r\n07/07/2020  09:13 pm               682 4.8.Threading.py\r\n11/06/2020  03:04 pm               252 4.9.temperature.csv\r\n 


# Example 3
# data_read.py file is available in repository. Make sure it's available in current working directory
import subprocess
# it will read data and store in theproc variable
theproc = subprocess.check_output("python chapter_12th_data_read.py", shell = True)
print(theproc) # to see the output of theproc
