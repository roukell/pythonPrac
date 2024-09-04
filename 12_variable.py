# variable name:
#   is case-sensitive
#   can include alphanumeric character and underscore
#   cannot start with a letter or underscore

# In python, variables are labels or tags that refer to objects in the python interpreter's namespace
a = [1, 2, 3]
b = a
c = b
b[1] = 0
print(a, b, c)

# here variables are referring to constants/immutable values
x = 1
y = x
z = y
y = 0
print(x, y, z)

# python variables can be set to any object
i = "hello"
print(i, type(i))

i = 0
print(i, type(i))

i = 3.14159
print(i, type(i))

# del statement deletes the variable (but not necessarily the object it was attached to)
del i
# here expecting a nameError(exception)
print(i)
