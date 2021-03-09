def scramble(s1, s2):
    from collections import Counter

    s1_count = Counter(s1)
    s2_count = Counter(s2)

    return all([value <= s1_count[letter] for letter, value in s2_count.items()])


print(scramble("rkqodlw", "world"))
