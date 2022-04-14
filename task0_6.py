def maximum(*args):
    max_number_holder = None
    for x in args:
        if max_number_holder == None:
            max_number_holder = x
        elif x > max_number_holder:
            max_number_holder = x
    return max_number_holder

print(maximum(-2,1,-5))
