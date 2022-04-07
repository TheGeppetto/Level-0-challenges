def maximum(*args):
    max_number_holder = [""]
    for x in args:
        if max_number_holder[0] == "":
            max_number_holder[0] = x
        elif x > max_number_holder[0]:
            max_number_holder[0] = x
    return max_number_holder[0]

print(maximum(-2,-2,-5))
