# https://dev.to/teosoft7/advanced-python-for-more-attractive-code-5fc1
# 1. Underscore(_) separator for Large Number

profit = 10000000
print(profit)

profit = 10_000_000

print(profit)

print(f"{profit:,}")

print("*" * 10, "1. HOW TO ROUND IN f STRING PYTHON", "*" * 10)

# how to round in f string python
profit = 10_000_000.914949

print(f"{profit:.2f}")

print("*" * 10, "2. ASSIGN a VALUE WITH if STATEMENT", "*" * 10)

# 2. Assign a value with if statement

UNDERAGE = 18

age = 15
status = "Adult" if age >= UNDERAGE else "Still Under Age"

print(status)

print("*" * 10, "3. Swap values between two variable", "*" * 10)

# 3. Swap values between two variable
row = 10
col = 3

print("Row", row)
print("Col", col)

temp = row
row = col
col = temp

print("Row", row)
print("Col", col)


# 4. Enumerate function
print("*" * 10, "4. Enumerate function", "*" * 10)

fields = [
    "username",
    "password",
    "email",
    "gender",
    "is_super",
]

counter = 100
for field in fields:
    print(counter, field)
    counter += 1

print("#########")

for counter, field in enumerate(fields, start=100):
    print(counter, field)


print("*" * 10, "5. List Comprehensions", "*" * 10)

numbers = [5, 8, 9, 12, 15, 3]

double = [num * 2 for num in numbers]

print(numbers)
print(double)

# 6. Unpacking

themes = ("dark", "white", "red", "green")
shape = (50, 7)
d, w, r, g = themes

print(themes)

print(d)
print(w)
print(r)
print(g)

print("######")
rows, cols = shape

print(shape)
print(rows, cols)
