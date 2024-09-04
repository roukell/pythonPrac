filename = "my_file.txt"

try:
    f = open(filename, "r")
    for line in f:
        print(line)
except Exception as e:
    raise e
finally:
    f.close()


with open(filename, "r") as f:
    for line in f:
        print(line)

