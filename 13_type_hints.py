# mixing incompatible types of objects will cause a runtime exception,
# but it will not raise an error at compile time
# type hints are used to reduce confusion

def add_ints(x: int, y: int) -> int:
    return x + y


# the following with type float does not throw an error
p: int = 3.5
z = add_ints(1, 2)
w = add_ints(1.0, 1.1)

print(p, z, w)
