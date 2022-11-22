def divide_or_square(number):
    if number % 5 == 0:
        return number ** 2
    else:
        return number % 5

print(divide_or_square(7))


# extra
# Get the longest value in a dictionary
def get_longest_value(dictionary):
    return max(dictionary.values(), key=len)

print(get_longest_value({'a': 'apple', 'b': 'banana', 'c': 'cherry', 'd': 'sniphermarube'}))