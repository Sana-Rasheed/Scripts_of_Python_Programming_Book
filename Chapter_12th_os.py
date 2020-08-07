# Example 1
# Before executing this example, create tempdir folder in C:// directory 
import os
os.chdir("C:\\tempdir")


# Example 2
os.getcwd() # get Current Working Directory
# output: 'C:\\tempdir'


# Example 3
os.chdir("C:\\tempdir")
os.getcwd()
# output: 'C:\\tempdir'
os.chdir("..")
os.getcwd()
# output: 'C:\\'


# Example 4
os.chdir("tempdir") 
os.getcwd()
# output: 'C:\\tempdir'

os.rmdir("C:\\tempdir")
# Output
# PermissionError: [WinError 32] The process cannot access the file 
# because it is being used by another process: 'C:\\tempdir'



# Example 
# try any one from below in terminal. 
os.listdir("C:\python37") # if you have this folder in C drive
# os.listdir("C:\Windows")

# Output of python37 folder:   
# ['DLLs', 'Doc', 'fantasy-1.py', 'fantasy.db', 'fantasy.py', 'frame.py', 'gridexample.py', 
# 'include', 'Lib', 'libs', 'LICENSE.txt', 'listbox.py', 'NEWS.txt', 'place.py', 'players.db',
# ,'tcl', 'test.py','© 'python3.dll', 'python36.dll', 'pythonw.exe', 'sclst.py', 'Script,    'python.exe',
# 'Tools', 'tooltip.py', 'vcruntime140.dll', 'virat.jpg', 'virat.py']
