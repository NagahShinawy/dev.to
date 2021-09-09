# https://dev.to/duomly/20-useful-python-tips-and-tricks-you-should-know-3h8c

import this

row = col = 5

print("#" * 100)

print(row, col)

print("#" * 100)

# 3. Chained Comparison

month = 13

is_valid = 1 <= month <= 12

print(is_valid)

# 4. Multiple Assignment

row, col, size = 4, 5, 100  # unpacking

print(row, col, size)

THEMES = ("black", "white", "red", "yellow", "blue")

blk, wht, *others = THEMES

print(blk, wht)
print(others)  # list of other items

print("#" * 100)
# 6. Swap Variables

row = 10
col = 8

print(row, col)

temp = row
row = col
col = temp

print(row, col)

width = 9

height = 5

print(width, height)

width, height = height, width
print(width, height)

# 7. Merge Dictionaries

profile = {"username": "john", "email": "john@test.com", "dob": "13-05-1999"}

vital_sign = {
    "tall": "170cm",
    "weight": "80kg",
}

full_info = profile.update(vital_sign)

print(full_info)  # None

print(
    profile
)  # {'username': 'john', 'email': 'john@test.com', 'dob': '13-05-1999', 'tall': '170cm', 'weight': '80kg'}

full_info = {**profile, **vital_sign}

print(
    full_info
)  # {'username': 'john', 'email': 'john@test.com', 'dob': '13-05-1999', 'tall': '170cm', 'weight': '80kg'}

# 9. Advance Iteration

print("#" * 100)

top_users = ["John", "Adam", "James", "Smith"]

for counter, user in enumerate(top_users, start=1):
    print(counter, user)

# 10. Reversed Iteration

path = ("Cairo", "Alex", "Matroh")

print(path)

back = path[::-1]

print(back)

# 11. Aggregate Elements

names = ["Loen", "Smith", "John"]
grades = [6, 8, 5]

info = zip(names, grades)  # [('Loen', 6), ('Smith', 8), ('John', 5)]

# print(list(info))

for name, grade in info:
    print(name, grade)


# 14. Sort Sequences

degrees = [("John", 50), ("James", 20), ("Loen", 60), ("Smith", 90), ]

sorted_by_degree = sorted(degrees, key=lambda student: student[-1])

print(degrees)
print(sorted_by_degree)
