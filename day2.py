# converts the list of strings to a list of integers and sums them
def convert_add(l):
    return sum([int(i) for i in l])

print(convert_add(['1', '2', '3', '4', '5']))

# checks for duplicates in a list
def check_duplicates(l):
    # if there a duplicate return the duplicate value
    for i in l:
        if l.count(i) > 1:
            return i

    # if there are no duplicates return None
    return f"No duplicates in {l}"

print(check_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'apple', 'banana','apple', 'cherry']))
print(check_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



