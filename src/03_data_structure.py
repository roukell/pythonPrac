import random

# list
fruits = ["apple", "banana"]
print(fruits[0])

# add item
fruits.append("pear")

fruits.extend(["watermelon", "blueberry"])
print(fruits)

# use randint
random_int = random.randint(0, 4)
print(random_int)

# or use choice
print(f"the random fruit is: {random.choice(fruits)}")

# nested list
vegetable = ["broccoli", "cabbage"]
shopping_list = [fruits, vegetable]
print(f"the shopping list: {shopping_list}")

print(shopping_list[0][1])
