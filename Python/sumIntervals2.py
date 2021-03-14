def sum_of_intervals(intervals):
    s = []
    for i in intervals:
        s += list(range(i[0], i[1]))
        print(s)
    return set(s)


print(sum_of_intervals([[1, 4], [7, 10], [3, 5]]))
# print(
#     sum_of_intervals(
#         [
#             [-388, 401],
#             [-154, 193],
#             [-124, 404],
#             [-76, 169],
#             [2, 237],
#             [26, 245],
#             [82, 202],
#             [265, 497],
#             [354, 394],
#             [463, 465],
#         ]
#     )
# )
