def check_register(dictionary):
    for i in dictionary:
        if dictionary[i] == 'yes':
            # count the number of yes
            dictionary[i] = 1
        else:
            dictionary[i] = 0
    # return the sum of the yes
    return sum(dictionary.values())

print(check_register({'John': 'yes', 'Jane': 'no', 'Jack': 'yes', 'Jill': 'no', 'Joe': 'yes'}))

