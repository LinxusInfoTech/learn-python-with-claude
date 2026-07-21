# Functions with type hints
# The ": str" and ": int" tell Python what type each parameter should be
# The "-> str" says "this function returns text"

def greet(name: str) -> str:
    message = f"Hello, {name}!"
    return message

result = greet("Sachin")
print(result)

print("\n---\n")

# A function that does math
def add(a: int, b: int) -> int:
    result = a + b
    return result

sum1 = add(5, 10)
print(f"5 + 10 = {sum1}")

sum2 = add(100, 250)
print(f"100 + 250 = {sum2}")

print("\n---\n")

# A function that returns yes/no
def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False

print(f"Is 25 an adult? {is_adult(25)}")
print(f"Is 15 an adult? {is_adult(15)}")
