"""
This module count works in a file
"""


def words_occur():
    """
    words_occur() - count the occurrences of words in a file
    """
    # prompt user to type in file name
    file_name = input("Enter the name of the file: ")

    # open file --> read --> store words in a list --> close file
    f = open(file_name, "r")
    word_list = f.read().split()
    f.close()

    # count the number of occurrences of each word in the file
    # {} - dictionary or set - a list of key-value pairs (mutable)
    occurs_dict = {}
    for word in word_list:
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    print(f"File {file_name} has {len(word_list)} words ({len(occurs_dict)} are unique)")
    print(occurs_dict)


# if __name__ == '__main__':
#     words_occur()

# __name__ is a special variable assigned to the name of the Python module by the interpreter.
# if you invoked the module as a script, '__main__' will be assigned to the special variable '__name__'
# if the module is imported into another module, the string 'my_module' will be assigned to '__name__'
