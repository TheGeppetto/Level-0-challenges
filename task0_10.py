def common_characters(input_string1, input_string2):
    input_string1 = input_string1.lower()
    input_string2 = input_string2.lower()
    common_characters_list = []
    
    for x in input_string1:
        if x in input_string2:
            if x not in common_characters_list:
                common_characters_list.append(x)
            
    return "Common Letters: " + ", ".join(i for i in common_characters_list)

print(common_characters("Househ", "Homputersh"))
