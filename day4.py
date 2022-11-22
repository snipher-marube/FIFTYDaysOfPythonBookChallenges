def only_float(a, b):
    # check if a and b are floats
    if isinstance(a, float) and isinstance(b, float):
        # return 2 if both are floats
        return 2
    # if a or b is not a float
    elif not isinstance(a, float) or not isinstance(b, float):
        # return 1 if only one is a float
        return 1
    # if both are not floats
    else:
        # return 0 if both are not floats
        return 0

print(only_float(12, 2.4))

