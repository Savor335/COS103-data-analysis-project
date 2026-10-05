### 1. Print all prime numbers up to a given number

limit = int(input("Enter a number: "))

print(f"Prime numbers up to {limit}:")
for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()


### 2. Multiplication table using nested loops

size = int(input("Enter table size (e.g. 10): "))

for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{i * j:4}", end="")
    print()

### 3. Simple number guessing game

import random

secret = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts.")
        break