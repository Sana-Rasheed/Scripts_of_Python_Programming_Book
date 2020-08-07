# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:15:35 2020

@author: sana.rasheed
"""

### Chapter 16th - SQLite

# Example 1
# Create Database 
import sqlite3
try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')         
    cursor = sqliteConnection.cursor()      
    print("Database created and Successfully Connected to SQLite")      
    sqlite_select_Query = "select sqlite_version();"         
    cursor.execute(sqlite_select_Query)        
    record = cursor.fetchall()     
    print("SQLite Database Version is: ", record)     
    cursor.close()                  
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)                                    
     
finally:
    if (sqliteConnection):
       sqliteConnection.close()
       print("The SQLite connection is closed")

# Outputput 
# Database created and Successfully Connected to SQLite   
# SQLite Database Version is:  [('3.31.1',)]
# The SQLite connection is closed


# =========================================================
# Connect to Databse, Create Table and Close connection with Database.
import sqlite3
try:
     sqliteConnection = sqlite3.connect('SQLite_Python.db')      
     sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (      
                                  id INTEGER PRIMARY KEY,
                                  name TEXT NOT NULL,
                                  email text NOT NULL UNIQUE,
                                  joining_date datetime,
                                  salary REAL NOT NULL);'''
     cursor = sqliteConnection.cursor()   
     print("Successfully Connected to SQLite")   
     cursor.execute(sqlite_create_table_query)     
     sqliteConnection.commit()  
     print("SQLite table created")   
     cursor.close()   
except sqlite3.Error as error:
     print("Error while creating a sqlite table", error)
finally:
     if (sqliteConnection):   
        sqliteConnection.close()     
        print("sqlite connection is closed")

# Output 
# Successfully Connected to SQLite
# SQLite table created
# sqlite connection is closed


# =========================================================
# Connect to Database
import sqlite3
conn = sqlite3.connect('test.db')
print ( "Opened database successfully")


# =========================================================
# Connect to Database and Execute Query to Create COMPANY Table
import sqlite3
conn = sqlite3.connect('test.db')
print  ("Opened database successfully") 

conn.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
	         NAME           TEXT    NOT NULL,                      
        	 AGE            INT     NOT NULL,
          	 ADDRESS        CHAR(50),                      
                 SALARY         REAL);''')
print( "Table created successfully")    
conn.close()

# Output
# Opened database successfully
# Table created successfully


# =========================================================
# Connect to Database and INSERT DATA into COMPANY Tabele
import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit()
print ("Records created successfully")
conn.close()

# Output
# Opened database successfully
# Records created successfully

# NOTE: delete test.db if table already exists error occur, after executing conn.close()
# Alternatively, create new table and insert data

# =====================================================================

import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("Operation done successfully")
conn.close()

# Output

# Opened database successfully
# ID =  1
# NAME =  Paul
# ADDRESS =  California
# SALARY =  20000.0 
# ID =  2
# NAME =  Allen
# ADDRESS =  Texas
# SALARY =  15000.0 
# ID =  3
# NAME =  Teddy
# ADDRESS =  Norway
# SALARY =  20000.0 
# ID =  4
# NAME =  Mark
# ADDRESS =  Rich-Mond 
# SALARY =  65000.0 
# Operation done successfully


# ================================================

import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print ("Total number of rows updated :", conn.total_changes)
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("Operation done successfully")
conn.close()

# Output

# Opened database successfully
# Total number of rows updated : 1
# ID = 1
# NAME = Paul
# ADDRESS = California
# SALARY = 25000.0
# ID = 2
# NAME = Allen
# ADDRESS = Texas
# SALARY = 15000.0
# ID = 3
# NAME = Teddy
# ADDRESS = Norway
# SALARY = 20000.0
# ID = 4
# NAME = Mark
# ADDRESS = Rich-Mond
# SALARY = 65000.0
# Operation done successfully

# ======================================================================

import sqlite3
conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print ("Total number of rows deleted :", conn.total_changes)
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print( "ADDRESS = ", row[2])
   print( "SALARY = ", row[3], "\n")
print ("Operation done successfully")
conn.close()

# Output

# Opened database successfully
# Total number of rows deleted : 1
# ID = 1
# NAME = Paul
# ADDRESS = California
# SALARY = 20000.0
# ID = 3
# NAME = Teddy
# ADDRESS = Norway
# SALARY = 20000.0
# ID = 4
# NAME = Mark
# ADDRESS = Rich-Mond
# SALARY = 65000.0
# Operation done successfully
