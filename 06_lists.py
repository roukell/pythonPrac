x = []
x.append(0)
x.extend([1,2,3])
x.insert(0, 3)
x.pop(-2)
x.remove(3)
x.reverse()
x.sort()


index = x.index(0)
count = x.count(2)

# convert to tuple, which is immutable
tuple(x)

# convert tuple back to list
list(x)

print(x)
print(count)
print(index)
