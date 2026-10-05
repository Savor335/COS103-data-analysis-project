### 1. Reverse a string and check for palindromes


text = input("Enter a word or phrase: ")

reversed_text = text[::-1]
print("Reversed:", reversed_text)

# Ignore case, spaces and punctuation when checking
cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

if cleaned == cleaned[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

### 2. Practice different string methods


s = "  Python Programming is Fun  "

print(s.strip())                     # remove spaces at both ends
print(s.lower())                     # lowercase
print(s.upper())                     # uppercase
print(s.title())                     # Title Case
print(s.replace("Fun", "Awesome"))   # replace text
print(s.split())                     # split into a list of words
print(s.strip().startswith("Python"))  # True
print(s.strip().endswith("Fun"))       # True
print(s.count("o"))                  # count a letter
print(s.find("Programming"))         # index of first match

# Indexing and slicing
t = "Python"
print(t[0], t[-1])     # P n
print(t[0:3])          # Pyt
print(t[::2])          # Pto

# Formatting
name, mark = "Ade", 87.456
print(f"{name} scored {mark:.1f}")
print("{} scored {:.1f}".format(name, mark))

# Escape sequences
print("Line one\nLine two")
print("Name:\tAde")
print("She said \"Hello\"")
print("C:\\Users\\Ade")

### 3. Simple text-based Hangman game


import random

words = ["python", "program", "variable", "function", "string", "integer"]
word = random.choice(words)
guessed = []
attempts = 6

print("=== HANGMAN ===")

while attempts > 0:
    display = " ".join(letter if letter in guessed else "_" for letter in word)
    print(f"\nWord: {display}")

    if "_" not in display:
        print("Congratulations! You won!")
        break

    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed:
        print("You already guessed that letter.")
    else:
        guessed.append(guess)
        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
else:
    print(f"Game over! The word was '{word}'")

