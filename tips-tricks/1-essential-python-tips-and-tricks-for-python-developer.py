double = lambda x: x * 2

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

