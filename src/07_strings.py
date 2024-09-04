import re

x = """
print some stuff 
with a new line
pikachu
"""

y = "live and     let \t   \tlive"

print(x)
print(x.split())
print(x.replace("pikachu", "mu"))

regex = re.compile(r"[\t ]+")
result = regex.sub(" ", y)
print(result)

# backslashes can be used to escape characters to give them special meanings
# \n - newline
# \t - tab
# \\ - a single normal backslash character
# \" - plain double-quote character
z = "\tThis string starts with a \"tab\""
k = "This string contains a single backslash(\\)"
j = "This string has a newline \n NEW LINE"
print(z)
print(k)
print(j)

# single quote can be used
i = "hello"
m = 'hello'
n = "don't need a backslash"
o = 'can\'t get by without a backslash'
p = 'you can have a double quote " in your string'
q = """use double qoute " and
single qoute ' and
multiple lines
"""
print(i, m, n, o, p, q)

