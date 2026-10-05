### 1. Recursive function for the factorial of a number


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)   # recursive case

num = int(input("Enter a number: "))
print(f"{num}! = {factorial(num)}")


### 2. Decorator that logs function calls


import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(3, 5)
greet("Amigo", greeting="Hi")


### 3. Recursive algorithm for the Tower of Hanoi


def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

disks = int(input("Enter number of disks: "))
hanoi(disks, "A", "C", "B")
print(f"Total moves: {2 ** disks - 1}")
