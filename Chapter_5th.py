# Example 1
a = 33
b = 200
if b > a:
	print("b is greater than a")

# Output
# b is greater than a


# Example 2
a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")

# Output
# a and b are equal


# Example 3
a = 200
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
else:
	print("a is greater than b")

# Output
# a is greater than b


# Example 4
x = 41
if x > 10:
	print("Above ten,")
if x > 20:
	print("Also above 20!")
else:
	print("but not above 20.")

# Output
# Above ten,
# Also above 20!


# Example 5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x) 

# Output
# apple
# banana
# cherry


# Example 6
for x in "banana":
	print(x)

# Output
# b
# a
# n
# a
# n
# a


# Example 7
for x in range(6):
	print(x)
else:
	print("Finally finished!") 

# Output
# 0
# 1
# 2
# 3
# 4
# 5
# Finally finished!


# Example 8
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
	for y in fruits:
		print(x, y)
# Output
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry


# Example 9
i = 1
while i < 6:
	print(i)
	i += 1

# Output
# 1
# 2
# 3
# 4
# 5


# Example 10
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	if x == "banana":
		continue
	print(x)

# Output
# apply
# cherry


# Example 11
i = 0
while i < 6:
	i += 1
	if i == 3:
        	continue
	print(i)

# Output
# 1
# 2
# 4
# 5
# 6


# Example 12
fruits = ["apple", "banana", "cherry"]
for x in fruits:
	print(x)
	if x == "banana":
		break

# Output
# apply
# banana

# Example 13
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

# Output
# 1
# 2
# 3

# Example 14
for x in [0, 1, 2]:
	pass


