# WITHOUT a function (repetitive and boring)
print("--- Without a function (repetitive) ---")
print("Hello Alice! Welcome to the team.")
print("Hello Bob! Welcome to the team.")
print("Hello Charlie! Welcome to the team.")

print("\n--- WITH a function (clean) ---")

# Define the function ONCE
def greet(name):
    print(f"Hello {name}! Welcome to the team.")

# Use it many times
greet("Alice")
greet("Bob")
greet("Charlie")
