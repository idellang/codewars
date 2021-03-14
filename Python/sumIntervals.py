# use iterator
def sum_of_intervals(intervals):

    intervals = list(map(list, intervals))
    intervals.sort()

    merged = [intervals[0]]

    for current in intervals:
        previous = merged[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
            if current[0] <= previous[0]:
                previous[0] = min(current[0], previous[0])
        else:
            merged.append(current)

    merged = map(lambda x: x[1] - x[0], merged)
    return sum(merged)


print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))
print(
    sum_of_intervals(
        [
            [-388, 401],
            [-154, 193],
            [-124, 404],
            [-76, 169],
            [2, 237],
            [26, 245],
            [82, 202],
            [265, 497],
            [354, 394],
            [463, 465],
        ]
    )
)
