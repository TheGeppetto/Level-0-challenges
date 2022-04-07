def get_vowel(input_string):
    #I convert all the characters into lowercase and find the vowels and avoid repititions 
    input_string = input_string.lower()
    vowel_list = []
    for i in input_string:
        if i in ["a","e","i","o","u"]:
            if i not in vowel_list:
                vowel_list.append(i)
    return "Vowels: " + ", ".join(str(i) for i in vowel_list)

print((get_vowel("Umuzi")))
