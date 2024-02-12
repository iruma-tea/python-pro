from functools import reduce
squares = map(lambda x: x * x, [1, 2, 3, 4, 5])
for i in squares:
    print(i, end=" ")
print()

should = reduce(lambda x, y: x and y, [True, True, False])
print(should)
should = reduce(lambda x, y: x and y, [True, True, True])
print(should)

evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
for i in evens:
    print(i, end=" ")
print()
