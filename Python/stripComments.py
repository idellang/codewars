"""delete words after the sign"""


def solution(string, markers):
    import re

    patterns = []
    for marker in markers:
        patterns.append(f"\{marker}.?.*")

    for pattern in patterns:
        string = re.sub(pattern, "", string)

    # remove whitespice
    ans = []
    for string in string.split("\n"):
        ans.append(string.rstrip())

    return "\n".join(ans)