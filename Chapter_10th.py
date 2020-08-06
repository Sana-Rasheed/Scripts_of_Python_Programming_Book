# Example 1
# make sure you have demofile.txt file in your working directory
f = open("demofile.txt", "r")
print(f.read())

# OUT
# C:\Users\My Name>python demo_file_open.py 
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# Example 2
f = open("demofile.txt", "r")
print(f.read(5))

# OUT
# C:\Users\My Name>python demo_file_open2.py
# Hello

# Example 3
f = open("demofile.txt", "r")
print(f.readline())

# OUT
# C:\Users\My Name>python demo_file_readline.py
# Hello! Welcome to demofile.txt


#Example 4
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# OUT
# C:\Users\My Name>python demo_file_readline2.py
# Hello! Welcome to demofile.txt
# This file is for testing purposes.


# Example 4
f = open("demofile.txt", "r")
for x in f:
  print(x)


# OUT
# C:\Users\My Name>python demo_file_readline3.py
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

# Example 5

f = open("demofile.txt", "r")
print(f.readline())
f.close()

# OUT
# C:\Users\My Name>python demo_file_close.py
# Hello! Welcome to demofile.txt


# Example 6
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())                    


# OUT
# C:\Users\My Name>python demo_file_append.py
# Hello! Welcome to demofile2.txt
# This file is for testing purposes.
# Good Luck!Now the file has more content!


# Example 7
f = open("demofile3.txt", "w")
f.write(" I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())                


# OUT
# C:\Users\My Name>python demo_file_write.py
#  I have deleted the content!


# Example 8
import os    
os.remove("demofile.txt")

# Example 9
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# Example 10 
# Create myfolder in working directory before executing code below.
import os
os.rmdir("myfolder")
