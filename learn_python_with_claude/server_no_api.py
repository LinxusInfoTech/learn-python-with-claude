"""FastAPI server - Subscription mode (no API key needed)
Chat uses Claude web interface, not backend API calls
"""
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the assets directory
ASSETS_DIR = Path(__file__).parent / "assets"

# Lessons content
LESSONS = {
    "variables": {
        "title": "Variables: Labeled Boxes",
        "content": """
A variable is a labeled box that holds a value.

Think of it like a mailbox with a name on it:
- Box name: `name`
- Value inside: `"Sachin"`

In Python:
```python
name = "Sachin"
age = 28
is_coding = True
```

The `=` sign means "put this value in this box"

You can check what's in a box:
```python
print(name)     # Prints: Sachin
print(age)      # Prints: 28
```

Key rule: the variable name goes on the left, the value goes on the right.
        """
    },
    "types": {
        "title": "Types: Different Kinds of Values",
        "content": """
Every value in Python has a type. The main types are:

1. **str** (string) - Text
   ```python
   name = "Sachin"
   city = "Bangalore"
   ```

2. **int** (integer) - Whole numbers
   ```python
   age = 28
   year = 2026
   ```

3. **float** (floating point) - Decimal numbers
   ```python
   height = 5.9
   price = 19.99
   ```

4. **bool** (boolean) - True or False
   ```python
   is_learning = True
   is_done = False
   ```

You can check a value's type with `type()`:
```python
print(type("Sachin"))    # <class 'str'>
print(type(28))          # <class 'int'>
print(type(True))        # <class 'bool'>
```

Why does this matter? Because some operations only work on certain types.
You can add two numbers, but you can't add a number to text.
        """
    },
    "fstrings": {
        "title": "F-Strings: Combining Text",
        "content": """
F-strings let you put variables into text cleanly.

The `f` prefix means "format this string" and `{}` is where you put values:

```python
name = "Sachin"
age = 28

# Old way (messy):
print("My name is " + name + " and I am " + str(age) + " years old")

# F-string way (clean):
print(f"My name is {name} and I am {age} years old")
```

You can put any expression inside `{}`:
```python
x = 5
y = 10
print(f"The sum is {x + y}")  # Prints: The sum is 15

is_adult = True
print(f"Adult? {is_adult}")   # Prints: Adult? True
```

F-strings are your best friend for making readable output.
        """
    },
    "functions": {
        "title": "Functions: Reusable Code",
        "content": """
A function is code you write ONCE and use MANY TIMES.

Problem: You want to greet 5 people. Without functions:
```python
print("Hello Alice! Welcome!")
print("Hello Bob! Welcome!")
print("Hello Charlie! Welcome!")
print("Hello Diana! Welcome!")
print("Hello Eve! Welcome!")
```

Repetitive and boring. If you need to change "Welcome!", fix it 5 times.

Solution: Write it once with a function:
```python
def greet(name):
    print(f"Hello {name}! Welcome!")

greet("Alice")
greet("Bob")
greet("Charlie")
greet("Diana")
greet("Eve")
```

Much cleaner! Change it in one place.

Parts of a function:
- `def` = "define a new function"
- `greet` = function name (what you call it)
- `(name)` = parameter (the ingredient that changes)
- `:` = "here comes the code"
- indented code = what the function does

A function can have multiple parameters:
```python
def introduce(name, job):
    print(f"{name} works as a {job}")

introduce("Sachin", "Engineer")
introduce("Alice", "Manager")
```

Key insight: Functions let you avoid repetition. DRY = Don't Repeat Yourself.
        """
    }
}

@app.get("/")
def read_root():
    return FileResponse(ASSETS_DIR / "index_subscription.html")

@app.get("/api/lessons")
def get_lessons():
    return {
        "lessons": [
            {"id": key, "title": value["title"]}
            for key, value in LESSONS.items()
        ]
    }

@app.get("/api/lessons/{lesson_id}")
def get_lesson(lesson_id: str):
    if lesson_id not in LESSONS:
        return JSONResponse({"error": "Lesson not found"}, status_code=404)

    lesson = LESSONS[lesson_id]
    return {"id": lesson_id, "title": lesson["title"], "content": lesson["content"]}

@app.post("/api/prepare-chat")
async def prepare_chat(request: dict):
    """Prepare context for Claude web interface"""
    message = request.get("message", "")
    lesson_id = request.get("lesson_id", "")
    selected_text = request.get("selected_text", "")

    context = "I'm learning Python with an interactive app.\n\n"

    if lesson_id and lesson_id in LESSONS:
        context += f"**Current Lesson:** {LESSONS[lesson_id]['title']}\n\n"

    if selected_text:
        context += f"**Selected Code/Text:**\n```\n{selected_text}\n```\n\n"

    context += f"**My Question:** {message}"

    return {
        "ready": True,
        "message": context,
        "instruction": "Copy the above text, open Claude (claude.ai), paste it in the chat, and ask your question!"
    }
