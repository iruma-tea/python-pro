from functools import partial


def pow(x, power=1):
    return x ** power


square = partial(pow, power=2)
cube = partial(pow, power=3)

print(square(3))
print(cube(3))
print(square(8))
print(cube(8))
