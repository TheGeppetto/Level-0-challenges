def maximum(*args):
  #I used *arguments to accomodate any number of inputs
    max_number_holder = [0]
    for x in args:
        if x > max_number_holder[0]:
            max_number_holder[0] = x
    return max_number_holder[0]

print(maximum(1,2,3))
