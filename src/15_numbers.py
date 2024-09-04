# floating-point result with normal division
x = 5 / 2
print(x)

# floating-point result
y = 5 / 2.0
print(y)

# integer result with truncation when divided using //
z = 5 // 2
print(z)

# too large to be an int in many languages
m = 30000000000
print(m, type(m))

n = m * 3
print(n, type(n))

o = m * 3.0
print(o, type(o))

# scientific notation - float
p = 2.0e-8
print(p, type(p))

q = int(200.2)
print(q, type(q))

r = int(2e2)
print(r, type(r))

s = float(200)
print(s, type(s))

# built-in numeric func
# abs, divmod, float, hex, int, max, min, oct,
# pow, round

# advanced func
# from math import *
# acos, asin, atan, atan2, ceil, cos, cosh, e, exp, fabs, floor, fmod,
# frexp, hypot, ldexp, log, log10, mod, pi, pow, sin, sinh, sqrt, tan,
# tanh

# complex number
t = (3+2j)
print(t, type(t))
