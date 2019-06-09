import os


def check_vowels(string):
    counter = 0
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            counter += 1
            if counter == 3:
                return True
    return False


def check_bad_string(string):
    bad_elems = ("ab", "cd", "pq", "xy")
    for i in range(1, len(string), 2):
        if string[i - 1] + string[i] in bad_elems:
            return False
    return True


def check_double_letters(string):
    for i in range(1, len(string), 2):
        if string[i - 1] == string[i]:
            return True
    return False


def count_nice_strings(data):
    strings = data.split("\n")
    nice_strings = 0
    for string in strings:
        condition_1 = check_vowels(string=string)
        condition_2 = check_bad_string(string=string)
        condition_3 = check_double_letters(string=string)
        if condition_1 and condition_2 and condition_3:
            nice_strings += 1
    return nice_strings


if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, "input")
    with open(input_path, "r") as input_file:
        instructions = input_file.read()

    # Returns not enough
    print(count_nice_strings(data=instructions))
