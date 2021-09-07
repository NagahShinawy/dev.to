# https://dev.to/teosoft7/advanced-python-for-more-attractive-code-5fc1
# 1. Underscore(_) separator for Large Number

profit = 10000000
print(profit)

profit = 10_000_000

print(profit)

print(f"{profit:,}")


# how to round in f string python
profit = 10_000_000.914949

print(f"{profit:.2f}")

# 2. Assign a value with if statement

UNDERAGE = 18

age = 15
status = "Adult" if age >= UNDERAGE else "Still Under Age"

print(status)