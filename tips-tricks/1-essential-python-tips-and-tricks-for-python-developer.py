double = lambda x: x * 2


DAYS = 7
TEN = 10


print(double)  # <function <lambda> at 0x0000015298548798>

print(double(5))  # 10 ==> 5 * 2

numbers = [6, 7, 8, 2, 9]

doubles = map(lambda number: number * 2, numbers)  #
evens = filter(lambda number: number % 2 == 0, numbers)
odds = filter(lambda number: number % 2 != 0, numbers)


print(doubles)  # <map object at 0x0000029C0780FD88>
print(evens)  # <filter object at 0x000001CE6AA03D88>
print(odds)  # <filter object at 0x000001BD17C0D988

for num in doubles:
    print(num, end=" ")


print()
print("#" * 100)

for even in evens:
    print(even, end=" ")

print()


# SELF CALLED LAMBDA

plus3 = (lambda a: a+3)(8)

print(plus3)  # 11

# List Comprehension

doubles = [(num, num * 2) for num in numbers]

print(doubles)

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]


print(evens)
print(odds)

# Dict Comprehension

names = ["John", "Loen", "James", "Smiths", "Django", "PHP"]

length = {name: len(name) for name in names}

print(names)
print(length)


# Set Comprehension


langs = ("php", "html", "js", "css", "sql")

print(langs)

langs = {lang.upper() for lang in langs}

print(langs)
print(type(langs))  # set


def days():
    for day in range(1, DAYS + 1):
        yield day


dys = days()

print(dys)  # <generator object days at 0x00000212FF54D348>

print(dys.__next__())  # 1
print(dys.__next__())  # 2

for d in dys:
    print(d, end=" ")  # 3 4 5 6 7


print()
print("#" * 100)

ten = (num for num in range(1, TEN + 1))

print(ten)

for n in ten:
    print(n, end=" ")

print()

# Shorthand If Else

is_female = True

gender = "Female" if is_female else "Male"

print(gender)

# Tuple Unpacking

dimension = (3, 6, 10)

print(dimension)
width, height, depth = dimension

print(width)
print(height)
print(depth)

# String Concatenation with delimiter

emails = ["john@test.com", "james@test.com", "loen@test.com", "adam@test.com"]

recipients = ";".join(emails)

print(emails)
print(recipients)

commands = ("cd ..", "ls")

execute = " & ".join(commands)

print(execute)