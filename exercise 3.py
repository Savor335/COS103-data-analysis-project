### 1. Positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")


### 2. Password strength checker


password = input("Enter a password: ")

has_upper = any(db.isupper() for db in password)
has_lower = any(db.islower() for db in password)
has_digit = any(db.isdigit() for db in password)
has_special = any(not db.isalnum() for db in password)
lengthenough = len(password) >= 8

score = sum([has_upper, has_lower, has_digit, has_special, lengthenough])

if score == 5:
    print("Strong password")
elif score >= 3:
    print("Medium password")
else:
    print("Weak password")

if not lengthenough:
    print("- Use at least 8 characters")
if not has_upper:
    print("- Add an uppercase letter")
if not has_lower:
    print("- Add a lowercase letter")
if not has_digit:
    print("- Add a number")
if not has_special:
    print("- Add a special character (e.g. @, #, !)")

### 3. Simple grading system

score = float(input("Enter score (0 - 100): "))

if score < 0 or score > 100:
    print("Invalid score! Enter a value between 0 and 100")
elif score >= 70:
    print("Grade: A (Excellent)")
elif score >= 60:
    print("Grade: B (Very Good)")
elif score >= 50:
    print("Grade: C (Good)")
elif score >= 45:
    print("Grade: D (Fair)")
elif score >= 40:
    print("Grade: E (Pass)")
else:
    print("Grade: F (Fail)")