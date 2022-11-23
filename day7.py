def hide_password():
    password = input("Enter your password: ")
    # hide the password characters with *
    print(f"your password has {len(password)} characters")
    password = '*' * len(password)
    # return the password
    return password


print(hide_password())
# print the length of the password

