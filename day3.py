def check_register(dictionary):
    for i in dictionary:
        if dictionary[i] == 'yes':
            return len(i)
    return 'No one is registered'

print(check_register({'John': 'yes', 'Jane': 'no', 'Jack': 'yes'}))

