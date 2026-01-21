# Test 1: string iteration

name = "Nicole"

for c in name:
    print(c)

print()

# Test 2: list iteration and manipulation

class_items = ["notebook", "pen", "power supply"]
class_items.append("jacket")

for item in class_items:
    print(f"Item: {item}")

print()

# Test 3: tuple iteration

class_schedule = ("Math", "English", "Computer Science")

for course in class_schedule:
    print(f"Course: {course}")
# Test 4: range iteration

simple_range = range(10)
bounded_range = range(1, 11)
stepwise_range = range(0, 30, 5)

for num in simple_range:
    print(num)

print()

for num in bounded_range:
    print(num)

print()

for num in stepwise_range:
    print(num)
