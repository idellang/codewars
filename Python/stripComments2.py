def solution(string, markers):
    parts = string.split("\n")
    for marker in markers:
        for i in range(len(parts)):
            if marker in parts[i]:
                parts[i] = parts[i].split(marker)[0].rstrip()
    return "\n".join(parts)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))