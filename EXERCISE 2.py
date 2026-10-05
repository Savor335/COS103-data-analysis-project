print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Choose 1 or 2: ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"{c}°C = {f:.2f}°F")
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f"{f}°F = {c:.2f}°C")
else:
    print("Invalid choice")


### 2. Practice variable assignments and type checking

age = 15                 # int
height = 1.75            # float
name = "Amigo"           # str
is_student = True        # bool
z = 3 + 4j               # complex

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))
print(z, type(z))

# isinstance() checks a type and returns True/False
print(isinstance(age, int))        # True
print(isinstance(height, int))     # False

# Multiple assignment
a, b, c = 1, 2.5, "hello"
print(type(a), type(b), type(c))

# Type conversion (casting)
num_str = "100"
num = int(num_str)
print(num + 50, type(num))         # 150 <class 'int'>
print(float(age), str(height))     # 15.0 1.75


### 3. Area of different shapes based on user input


import math

print("Choose a shape: circle, rectangle, triangle")
shape = input("Shape: ").strip().lower()

if shape == "circle":
    r = float(input("Enter radius: "))
    area = math.pi * r ** 2
    print(f"Area of circle = {area:.2f}")
elif shape == "rectangle":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of rectangle = {area:.2f}")
elif shape == "triangle":
    base = float(input("Enter base: "))
    tri_height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"Area of triangle = {area:.2f}")
else:
    print("Unknown shape")