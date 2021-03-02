def pig_it(text):
    ans = []
    list_text = text.split(" ")
    for text in list_text:
        if text.isalpha():
            ans.append(text[1:] + text[0] + "ay")
        else:
            ans.append(text)

    return " ".join(ans)


print(pig_it("O tempora o mores !"))
