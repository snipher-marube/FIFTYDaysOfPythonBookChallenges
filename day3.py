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

# extra
# create a tuple that returns only lowercase names from a tuple leaving the uppercase names in the tuple
def get_lower_names(tup):
    return tuple([i for i in tup if i.islower()])

print(get_lower_names(('John', 'Jane', 'Jack', 'Jill', 'Joe', 'abel', 'baker', 'charlie', 'david', 'edward')))