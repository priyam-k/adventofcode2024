# day 2-1
# 1 line of code (excluding input processing)
# basically loops over each row, checks if differences b/w adjacent elements is b/w 1 and 3 and that the
# direction of difference stays consistent. uses ternaries and sums to count the number of valid rows

with open("day2_INPUT.txt") as f:
    data = f.readlines()
data = [list(map(int, x.strip().split())) for x in data]
# [(1 for l in r) for r in data]
# for r in data:
#     s = (r[1] - r[0]) / abs(r[1] - r[0])
#     sum(
#         [
#             0 if 1 <= abs(r[i + 1] - r[i]) <= 3 and (r[i + 1] - r[i]) / s > 0 else 1
#             for i in range(len(r) - 1)
#         ]
#     )

print(
    sum(
        (
            1
            if sum(
                [
                    (
                        0
                        if 1 <= abs(r[i + 1] - r[i]) <= 3
                        and r[1] - r[0] != 0
                        and (r[i + 1] - r[i]) / ((r[1] - r[0]) / abs(r[1] - r[0])) > 0
                        else 1
                    )
                    for i in range(len(r) - 1)
                ]
            )
            == 0
            else 0
        )
        for r in data
    )
)
