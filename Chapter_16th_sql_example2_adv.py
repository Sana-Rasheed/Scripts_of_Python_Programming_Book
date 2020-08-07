# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:38:33 2020

@author: sana.rasheed
"""

### Chapter 16th - SQLite
'''
Author NOTE:
    Few functions have been improved and not covered in book. 
    You can test it for your own learning. 
'''
# Example 3 - Advance implementation of Example 2 
# Functions implementated for quick DB connection and Table creations 
import sqlite3
from sqlite3 import Error 

# Function to open DB connection
def  create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try: 
         conn = sqlite3.connect(db_file)
         print("The SQLite connection is connected")
         return conn
    except Error as e:
         print(e)
    return conn

# Function to close DB connection
def  close_connection(conn):
    """ close database connection to the SQLite database specified by db_file
    :param db_file: database file
    """  
    if (conn):
         conn.close()
         print("The SQLite connection is closed")


# Function to create new table in DB
def  create_table_in_db(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """ 
    try:
         c = conn.cursor()
         c.execute(create_table_sql) 
    except Error as e:
         print(e)

# Create STUDENT Table  - MODIFIED
def  create_table(database):
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS STUDENTS (
                            		id integer PRIMARY KEY,
                           		name text NOT NULL,
                                        gpa integer,
                                        admission_date text
                                    	); """ 
    #  create a database connection
    conn = create_connection(database)
    
    #  create tables
    if conn is not None:
        # create projects table
         create_table_in_db(conn, sql_create_projects_table)
    else:
         print("Error! cannot create the database connection.")   
    close_connection(conn)


# main execution to create table 
database =  r"C:\\tempdir\database.db" # DB location
create_table(database) # parse db name to create table in it. 

# ======================================================

# Add student data in table
def  add_student(conn, student):
    """
    Create a new student entry into the student table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO STUDENTS(name,gpa,admission_date)
               VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    return cur.lastrowid    

# main function to add student in table - MODIFIED
def  main_function(student):
    database =r"C:\\tempdir\database.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
    #    add a new student
         student_id = add_student(conn, student)
    
    print('The Student ID:', student_id)
    close_connection(conn)

    
# Execute main funtion to add multiple students in table
student1 = ('Fahad', 3.4, '2019-1-30'); 
main_function(student1)
student2 = ('Munira', 2.9, '2012-2-30');
main_function(student2)
student3 = ('Khawar', 3.79, '2018-11-30');
main_function(student3)

# direct input to function to add new students
main_function(('Ahad', 3.33, '2019-12-03')) 
main_function(('Momina', 2.83, '2020-02-13')) 

# ==============================================================
### READ TABLE 
database = r"C:\\tempdir\database.db"
#create a database connection
conn = create_connection(database)
try:
    cursor = conn.cursor()
    table_name = "STUDENTS" 
    sql_string = "SELECT * from " + table_name
    sqlite_select_query = sql_string

    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Total rows are:  ", len(records))
    cursor.close()
except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    close_connection(conn)		
print(records)

