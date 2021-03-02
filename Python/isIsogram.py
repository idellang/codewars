def is_isogram(string):
    text = [ele for ele in string.lower() if ele.isalpha()]
    set_letters = {ele for ele in string.lower() if ele.isalpha()}
    return len(text) == len(set_letters)


print(is_isogram("Dermatoglyphics"))
print(is_isogram("ab  "))
print(is_isogram("mOse.."))
