def duplicate_encode(word):
    ans = ""
    for letter in word.lower():
        if word.lower().count(letter) == 1:
            # print(word.lower().count(letter), "(")
            ans += "("
        else:
            # print(word.lower().count(letter), ")")
            ans += ")"
    return ans


print(duplicate_encode("zzn!nGQ!Pn  "))