# day 2-2
# 1 line of code (excluding input processing)
# basically same as day 2-1 except instead of looping the logic over each row, it loops over a list of possible
# variations of each row according to the Problem Dampener (u can remove any one level) and applies the logic to
# each variation. if at least one variation is valid, the row is valid.

with open("day2_INPUT.txt") as f:
    data = f.readlines()
data = [list(map(int, x.strip().split())) for x in data]

print(
    sum(
        (
            1
            if sum(
                (
                    1
                    if sum(
                        [
                            (
                                0
                                if 1 <= abs(p[i + 1] - p[i]) <= 3
                                and p[1] - p[0] != 0
                                and (p[i + 1] - p[i])
                                / ((p[1] - p[0]) / abs(p[1] - p[0]))
                                > 0
                                else 1
                            )
                            for i in range(len(p) - 1)
                        ]
                    )
                    == 0
                    else 0
                )
                for p in [r[:i] + r[i + 1 :] for i in range(len(r))] + [r]
            )
            > 0
            else 0
        )
        for r in data
    )
)
