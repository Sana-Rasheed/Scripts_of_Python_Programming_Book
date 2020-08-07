# Example 1
import requests 
x = requests.get("https://github.com/")  

print(x)
print(x.status_code)

# Output
# <Response [200]>
# 200



# Example 2
import requests
res = requests.get('https://api.github.com/users/sana-rasheed')
print(res)
print(res.status_code)
data = res.json()
print("Followering: ", data['following'])
print("Followers: ", data['followers'])

# Output
# <Response [200]>
# 200
# Followering:  1
# Followers:  30



# Example 3
import requests
url='https://official-joke-api.appspot.com/jokes/programming/random'  
res = requests.get(url) # get API end-point response
data = res.json()[0] # convert response text into json format
for key in data:
      print(key,":",data[key])

# Output
# id : 74
# type : programming
# setup : Why do C# and Java developers keep breaking their keyboards?
# punchline : Because they use a strongly typed language.



# Example 4
import requests 
myobj = [('Ali', 56),('Ahmed', 87),('Amna', 76)]

r = requests.post("http://httpbin.org/post", data=myobj) # post data to API 
r # To show API response status
data = r.json() # convert response text into json format
d = data['form'] # Posted data available under form tag
print(d)

# Output
# {'Ahmed': '87', 'Ali': '56', 'Amna': '76'}
