# Store some values
name = "Sachin"
age = 25

# Combine text with +
print("My name is " + name)

# You can combine multiple things
print("I am " + name + " and I am " + str(age) + " years old")

# But that gets messy. Here's a better way: f-strings
# The f means "format this string" and {} lets you put values inside
print(f"My name is {name} and I am {age} years old")
