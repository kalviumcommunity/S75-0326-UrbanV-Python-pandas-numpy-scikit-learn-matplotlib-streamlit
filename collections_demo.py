# 1. LIST EXAMPLE
print("=== LIST EXAMPLE ===")
fruits = ["apple", "banana", "cherry"]

# Access
print("First fruit:", fruits[0])

# Modify
fruits[1] = "orange"

# Add
fruits.append("grape")

# Remove
fruits.remove("apple")

print("Updated list:", fruits)


# 2. TUPLE EXAMPLE
print("\n=== TUPLE EXAMPLE ===")
colors = ("red", "green", "blue")

# Access
print("First color:", colors[0])

# Immutability demonstration
try:
    colors[1] = "yellow"  # This will raise an error
except TypeError as e:
    print("Error (tuples are immutable):", e)


# 3. DICTIONARY EXAMPLE
print("\n=== DICTIONARY EXAMPLE ===")
student = {
    "name": "Shankar",
    "age": 20,
    "course": "CSE"
}

# Access
print("Student name:", student["name"])

# Modify
student["age"] = 21

# Add
student["grade"] = "A"

print("Updated dictionary:", student)


# 4. CHOOSING DATA STRUCTURES
print("\n=== WHEN TO USE WHAT ===")
print("List → dynamic data (e.g., fruits)")
print("Tuple → fixed data (e.g., colors)")
print("Dictionary → structured data (e.g., student info)")