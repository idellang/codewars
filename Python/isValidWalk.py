def is_valid_walk(walk):
    x_dir = {"n": 1, "s": -1}
    y_dir = {"e": 1, "w": -1}
    x = []
    y = []
    for move in walk:
        x.append(y_dir.get(move, 0))
        y.append(x_dir.get(move, 0))

    return sum(x) == 0 and sum(y) == 0 and len(walk) == 10


print(is_valid_walk(["s", "w", "n", "w", "n", "e", "s", "e"]))
