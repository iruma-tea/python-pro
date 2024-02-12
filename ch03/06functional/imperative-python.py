squares = [x * x for x in [1, 2, 3, 4, 5]]
for i in squares:
    print(i, end=" ")
print()

should = all([True, True, False])
print(should)
should = all([True, True, True])
print(should)

evens = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]
for i in evens:
    print(i, end=" ")
print()
