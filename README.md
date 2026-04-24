# Python_Module_42

A class is user defined template “for creating objects” it holds **data** and **functions**

![image.png](attachment:b6934931-8424-4062-a663-b65c8456b3b1:image.png)

- 👉 Example:

```python
# define a class
class Dog:
    sound = "bark"  # class attribute
    
'''
// CLass

- The class keyword is how u declare a class
- The Dog keyword is how u name one 

// MEANWHILE 

The sound keyword is how a variable
 - that holds the "bark" string
'''
```

# 🧠 What is a *class* (idea first)

A **class** is like a **blueprint**.

👉 Imagine:

- A class = *plan of a house*
- An object = *actual house built from the plan*

So:

- Class defines **what something is**
- Object is the **real thing you create**

# 🧱 Why classes exist

Without classes → messy code

With classes → you can group:

- data (variables)
- behavior (functions)

👉 Example:

A “Dog” has:

- name
- color
- Eye_color
- ……………

Instead of separate variables/functions → put them in ONE class

# 🚗 A Car example :

```python
class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def drive(self):
        print("The car is moving")
```

# ⚫ CONCLUSION :

A **class** defines what an **object** should look like, and **an object** is created based on that **class**. For example:

## LEARNING PYTHON

### The Python interpreter

When you run `python3 ft_garden_data.py`, Python reads your file top to bottom and **executes** it. That **reading+executing** tool is called the **interpreter**. It's different from C where you compile first in Python, there's no separate compile step.

---

The `__main__` Environment

The top-level environment is the scope where the first user-specified Python module executes. It is "top-level" because it acts as the entry point that imports all other necessary modules. **Python documentation +2**

[Python documentation](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAkFBMVEX/////6HP/3VRBf7E/fa46dqY9eao4c6NGhrj/76D/7ZRDgrQxapn/5Gf/4F7/4mL/3FH/6Zrr8viQuNddlcFckLqbutN3p86mxd1xoceJq8hqm8JWh6+uyuDy9/tQgKj//fOZvtv/8LD/6YBolLmVscmyx81pl7z/2Eb/3mR+pcT/64b/1D3/43n/4HD/5YXqXVBAAAAAqUlEQVQYlUWO2xqCIBCEFzwfQFFDzUqTSjOh93+7Vi5orvaf2d1vAFBV3WTeSYJT2/WeHwZnZzT1gBxdnHHtpAyiaLRwa+M48zCP8jEh6QT3g/0QGQ3GZhgc55tiXIPl8YF6zgWnFGLk15yiSEFpWULjh0tCCGEYl+v6BhkG24cwxi3vAqp+kQpjpbUxRk+2i8J15K9rqvHbagR3RnpcG/HfAMH3nQo7/gCZEQ4WPNSeSwAAAABJRU5ErkJggg==)

`if __name__ == "__main__":`

Every Python file has a hidden variable called `__name__`. Its value depends on **how the file is used**:

```
You run it directly   →  __name__ == "__main__"
Another file imports it →  __name__ == "ft_garden_data"  (the filename)
```

So this block:

python

```python
if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
```

means: *"only run this code if I am the main program being executed, not if someone imports me."*

Why does that matter? Later in the project, exercise 2 will **import** your Plant class from exercise 1. If your test code wasn't inside that guard, it would run automatically during the import — which you don't want.

Class has object has attributes 

Class = Car 

object = name

attributes = BMW

### `self` — the instance

When you create an object and call a method on it, Python automatically passes that **specific object** as the first argument. By convention it's named `self`.

python

```python
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
# Python actually runs: Flower.show(rose)
#                                    ^^^^
#                               this is self
```

So inside `show()`, `self` is literally the `rose` object. That's how it knows whose name and height to print.

### `cls` — the class itself

In a `@classmethod`, Python passes the **class** as the first argument instead of an instance. By convention it's named `cls`.

python

```python
@classmethod
def create_anonymous(cls):
    return cls("Unknown plant", 0.0, 0)
```

One sentence each

> **`self`** — "which specific object is running this method right now?"
> 

> **`cls`** — "which class is this method being called on right now?"
> 
> 
> Think of it like this — if `Flower` is a cookie cutter and `rose` is a cookie:
> 
> - `cls` = the cookie cutter
> - `self` = a specific cookie made from it

# **🌋 Erors on both try and expect**

### Common errors you'll encounter

**`ValueError`** — right type, wrong value

```python
int("hello")        # "hello" is a string but can't become an int
int("12.5")         # same problem
```

**`ZeroDivisionError`** — dividing by zero

```python
10 / 0
```

**`FileNotFoundError`** — opening a file that doesn't exist

```python
open("ghost.txt")
```

**`TypeError`** — wrong type entirely

```python
"hello" + 5         # can't add a string and an int
len(42)             # 42 has no length
```

**`IndexError`** — accessing a list position that doesn't exist

```python
my_list = [1, 2, 3]
my_list[10]         # there's no index 10
```

**`KeyError`** — accessing a dict key that doesn't exist

```python
my_dict = {"name": "Rose"}
my_dict["color"]    # "color" key doesn't exist
```

**`AttributeError`** — calling something that doesn't exist on an object

```python
rose = Flower("Rose", 15.0, 10, "red")
rose.fly()          # Flower has no fly() method
```

**`NameError`** — using a variable you never defined

```python
print(banana)       # banana was never created
```

Last but not - least 

- `Exception` is used as a **safety net** — it catches everything. This is fine for small scripts, but in bigger programs you'd be more specific so you don't accidentally hide unexpected bugs.