def descending_order(num):
    num_list = sorted(list(str(num)), reverse=True)
    ans = "".join(num_list)
    return int(ans)


print(descending_order(42145))