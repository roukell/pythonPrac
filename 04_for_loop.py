import random

scores = [100, 98, 70, 80]

total_score = sum(scores)
print(total_score)

max_score = max(scores)
print(max_score)

total = 0
largest_num = 0

for i, score in enumerate(scores):
    print(f"current score is: {score}")
    total += score

    if score > largest_num:
        largest_num = score

    # if it is the last element, do something
    if i == len(scores) - 1:
        print(f"this is the last element index: {i}")

print(f"total score is: {total}")
print(f"max score is: {largest_num}")

# range function
total = 0
for num in range(1, 101):
    total += num
print(f"total is: {total}")

# add item to a list
my_list = ["dress", "pants"]
my_list.append("jacket")
print(my_list)

# shuffle list
random.shuffle(my_list)
print(my_list)



