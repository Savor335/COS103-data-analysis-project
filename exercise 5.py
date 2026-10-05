### 1. Contact book using a dictionary

contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone number: ").strip()
        contacts[name] = phone
        print("Contact saved.")
    elif choice == "2":
        if not contacts:
            print("No contacts yet.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "3":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"{name}: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")


### 2. Practice list and set operations


# ----- LISTS -----
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")            # add to end
fruits.insert(1, "orange")        # insert at index
fruits.remove("banana")           # remove by value
last = fruits.pop()               # remove and return last item
fruits.sort()                     # sort in place
print(fruits, last)
print(fruits[0], fruits[-1], fruits[0:2])   # indexing and slicing
print(len(fruits), "apple" in fruits)

# ----- TUPLES (immutable) -----
point = (3, 4)
print(point[0], point[1])
# point[0] = 10   # would raise TypeError

# ----- SETS -----
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # union: {1, 2, 3, 4, 5, 6}
print(a & b)    # intersection: {3, 4}
print(a - b)    # difference: {1, 2}
print(a ^ b)    # symmetric difference: {1, 2, 5, 6}
a.add(10)
a.discard(1)
print(a)

# Remove duplicates from a list using a set
nums = [1, 2, 2, 3, 3, 3]
print(list(set(nums)))

### 3. Student names and scores: highest score, average, names in alphabetical order


n = int(input("How many students? "))
students = {}

for i in range(n):
    name = input(f"Enter name of student {i + 1}: ").strip()
    score = float(input(f"Enter score for {name}: "))
    students[name] = score

highest_name = max(students, key=students.get)
highest_score = students[highest_name]
average = sum(students.values()) / len(students)

print(f"\nHighest score: {highest_score} ({highest_name})")
print(f"Average score: {average:.2f}")
print("Names in alphabetical order:")
for name in sorted(students):
    print("-", name)