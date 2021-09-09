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
