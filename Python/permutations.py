def permutations(string):
    import itertools

    ans = set()
    permuted = list(itertools.permutations(string, len(string)))
    for item in permuted:
        ans.add("".join(item))
    return list(ans)


print(permutations("abba"))