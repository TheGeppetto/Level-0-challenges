def common_characters(input_string1, input_string2):
    common_characters_list = []
    for x in input_string1:
        if x in input_string2:
            common_characters_list.append(x)
    return "Common Letters: " + ", ".join(str(i) for i in common_characters_list)

print(common_characters("house", "computers"))
