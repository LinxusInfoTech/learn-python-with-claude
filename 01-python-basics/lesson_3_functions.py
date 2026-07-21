# Define a function (write the recipe once)
def greet(name):
    print(f"Hello, {name}!")

# Use it many times (follow the recipe)
greet("Sachin")
greet("Alice")
greet("Bob")

print("\n---\n")

# Functions can take multiple parameters (ingredients)
def describe_person(name, age, job):
    print(f"{name} is {age} years old and works as a {job}")

describe_person("Sachin", 25, "Software Engineer")
describe_person("Alice", 30, "Product Manager")
describe_person("Bob", 22, "Designer")
