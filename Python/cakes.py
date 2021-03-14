"""return cakes that could be made"""


def cakes(recipe, available):
    portion = []
    for item in recipe:
        if item in available:
            portion.append(int(available.get(item) / recipe.get(item)))
        else:
            return 0
    return min(portion)


print(
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
)
