## 1. Function that returns a new list with each number squared


def square_list(numbers):
    return [n ** 2 for n in numbers]

print(square_list([1, 2, 3, 4, 5]))   # [1, 4, 9, 16, 25]

### 2. Practice using lambda functions and map/filter


# Lambda
add = lambda a, b: a + b
print(add(3, 4))                      # 7

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(): apply a function to every item
squares = list(map(lambda x: x ** 2, nums))
print(squares)

# filter(): keep items that pass a test
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Combine both: squares of the odd numbers
odd_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, nums)))
print(odd_squares)


### 3. Sort a list of dictionaries by a specified key using a lambda


students = [
    {"name": "Ade", "age": 15, "score": 78},
    {"name": "Bola", "age": 14, "score": 92},
    {"name": "Chidi", "age": 16, "score": 65},
]

key = input("Sort by (name / age / score): ").strip().lower()

if key in students[0]:
    sorted_list = sorted(students, key=lambda d: d[key])
    for s in sorted_list:
        print(s)
else:
    print("Invalid key")