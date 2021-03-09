def order(sentence):
    import re

    order = []
    sentence_list = sentence.split()
    for word in sentence_list:
        number = re.search("(([0-9.*]))", word)
        order.append(int(number.group(1)))

    ans = []
    for order, word in sorted(list(zip(order, sentence_list))):
        ans.append(word)

    return " ".join(ans)


# print(order("is2 Thi1s T4est 3a"))


def order2(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
