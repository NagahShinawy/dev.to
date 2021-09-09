# https://dev.to/worldindev/6-python-tips-tricks-that-no-one-teaches-4j73
import random
import datetime


answers = ["A", "B", "C", "D", "E"]

books = ["Harry potter", "Don Quixote", "Learn Python", "Dracula"]

book = random.choice(books)

for _ in range(10):
    answer = random.choice(answers)
    print(answer)


# Unpacking elements with *

print(*answers, sep="")

name = "John"

chars = [*name]  # [*iterable]
print(chars)  # ['J', 'o', 'h', 'n']

# https://dev.to/jerrynsh/3-useful-python-f-string-tricks-you-probably-don-t-know-2o54

# 1. F-string for Debugging


now = datetime.datetime.now()

print(now)


# usual way
dt = now.strftime("%Y-%m-%d")
print(dt)

# using f-string

dt = f"{now:%y-%m-%d %H:%M:%S}"

print(dt)


# A repr() alternative with f-string
print(now)
print(
    f"{now!r}"
)  # !r: means use __rep__ ==>  datetime.datetime(2021, 9, 9, 13, 50, 50, 247020)
