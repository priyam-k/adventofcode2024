# day 1-2
# 2 lines of code (excluding input processing)
# basically separates inputs into 2 column lists, multiplies element from lst1 with # occurences of it in lst2 and sums

with open("day1_INPUT.txt") as f:
    data = f.readlines()
data = [list(map(int, x.strip().split())) for x in data]
lst1, lst2 = [x[0] for x in data], [x[1] for x in data]
print(sum(i * lst2.count(i) for i in lst1))
