def funct(x, y=1, z=1):
    return x + 2 * y + z ** 2


def funct1(x, y=1, z=1, *tup):
    print((x, y, z) + tup)


def funct2(x, y=1, z=1, **kwargs):
    print(x, y, z, kwargs)


# result = funct(3, z=5, y=0)
# print(result)

# funct1(2, 0, 0, [3, 2, 1])

funct2(1, 0, 2, i=0, my_keyword="hello", my_keyword2="world")
