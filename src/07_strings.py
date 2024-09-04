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

# backslashes can be used to escape characters
