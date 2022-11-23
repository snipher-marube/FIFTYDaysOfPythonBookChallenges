# username generator from user email input
def username_generator():
    email = input("Enter your email: ")
    # get the name from the email before the @
    name = email[:email.index('@')]
    # check if the name has a dot
    if '.' in name:
        # split the name by the dot
        name = name.split('.')
        # join the name with a space
        name = ' '.join(name)
    # return the name
    return name

#print(username_generator())


# password generator from user email input
def password_generator():
    email = input("Enter your email: ")
    # get the name from the email before the @
    name = email[:email.index('@')]
    # get the domain from the email after the @
    domain = email[email.index('@') + 1:]
    # return the password
    return name + domain

#print(password_generator())


# extra
# create a function that takes a list of numbers and then zero out the first and last element of the list
def zero_out_list(lst):
    # check if the list has more than 2 elements
    if len(lst) > 2:
        # zero out the first and last element
        lst[0] = 0
        lst[-1] = 0
    # return the list
    return lst

print(zero_out_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

