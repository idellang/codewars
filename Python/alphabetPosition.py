def alphabet_position(text):
    import string

    text = text.lower()
    ans = []

    string_int_dict = dict(zip(string.ascii_lowercase, range(1, 28)))

    for letter in text:
        value = str(string_int_dict.get(letter, ""))
        if value:
            ans.append(value)
        else:
            pass
    return " ".join(ans)


def alphabet_position2(text):
    import string

    text = text.lower()
    ans = ""
    string_int_dict = dict(zip(string.ascii_lowercase, range(1, 28)))

    ans = [str(string_int_dict[letter]) for letter in text if letter.isalpha()]
    return " ".join(ans)


print(alphabet_position2("The sunset sets at twelve o' clock."))