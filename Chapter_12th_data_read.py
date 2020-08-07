# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:54:08 2020

@author: sana.rasheed
"""


# Example 
import csv
file = "Score.csv"
reader = csv.reader(open(file, 'r'))
for row in reader:
    print(row)
    