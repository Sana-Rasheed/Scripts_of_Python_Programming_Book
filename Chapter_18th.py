
# ******************* Execute Examples in terminal ********************* #
# Example 1
##################### 
### Read INI file ###    
#####################
import configparser
config = configparser.ConfigParser()
# give the correct path of spyder.ini file
config.read("C:\\Users\sana.rasheed\.spyder-py3\config\spyder.ini") #("C:\\Users\.spyder-py3\spyder.ini") 
config.sections()
print( config.sections() )
# Output
# ['main', 
#  'internal_console',
#  'main_interpreter',
#  'ipython_console',
#  'variable_explorer',
#  'plots',
#  'editor',
#  'historylog',
#  'help',
#  'onlinehelp',
#  'outline_explorer',
#  'project_explorer',
#  'explorer',
#  'find_in_files',
#  'breakpoints',
#  'profiler',
#  'pylint',
#  'workingdir',
#  'shortcuts',
#  'appearance',
#  'lsp-server',
#  'fallback-completions',
#  'kite']

[option for option in config['help']] 
print( [option for option in config['help']] )

# Output
# ['enable',   
#  'max_history_entries',
#  'wrap',
#  'connect/editor',
#  'connect/ipython_console',
#  'math',
#  'automatic_import',
#  'rich_mode',
#  'first_time']




# Example 2
##########################     
### Create Dictionary ###     
#########################
parser = configparser.ConfigParser()
parser.read_dict(
    {'section1': 
        {'tag1': '1','tag2': '2','tag3': '3'},
    'section2': 
        {'tagA': 'A','tagB': 'B','tagC': 'C'},
    'section3': 
        {'foo': 'x','bar': 'y','baz': 'z'} })
parser.sections()  #['section1', 'section2', 'section3']
print(parser.sections())

# Output
# ['section1', 'section2', 'section3']

[option for option in parser['section1']]
print([option for option in parser['section1']])

# Output
# 'tag1', 'tag2', 'tag3' 




# Example 3
############################## 
### Read Text/String file ###      
#############################
sample_config = """
[My Settings]
user = username
profile = /my/directory/to/profile.png
gender = male
[My new Settings]
user = Sana.Rasheed
profile = /my/directory/to/profile.png
gender = female
"""

# creates an instance of ConfigParser called config 
config = configparser.ConfigParser()  

#read the instance of string using read_string() method
config.read_string(sample_config)
config.sections()  #['My Settings']         
print(config.sections())
# Output
# ['My Settings', 'My new Settings']

                 
user = config["My new Settings"]["user"]  #'username'
print(user)

# Output
# 'Sana.rasheed'

