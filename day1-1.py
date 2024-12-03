# day 1-1
# 2 lines of code (excluding input processing)
# basically separates inputs into 2 column lists and sorts them, finds diff b/w each pair and sums

with open("day1_INPUT.txt") as f:
    data = f.readlines()
data = [list(map(int, x.strip().split())) for x in data]
lst1, lst2 = sorted([x[0] for x in data]), sorted([x[1] for x in data])
print(sum(abs(lst1[i] - lst2[i]) for i in range(len(lst1))))
