# coding:utf-8
"""
顺丰快递每天能收到成千上万的物流单，每个物流单的重量不一。
现在顺丰快递的货车司机隔壁老王开着顺丰的标配货车（限载5吨，含5吨，不考虑限高）,
想要一次性拿走尽可能重的货物，这些货有红木沙发，有钢材等等。
"""

conduct = [509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]


def solv(i, j):
    if i < 0:
        return 0
    if j > conduct[i]:
        cmp1 = solv(i - 1, j)
        cmp2 = solv(i - 1, j - conduct[i]) + conduct[i]
        return max(cmp1, cmp2)
    else:
        return solv(i - 1, j)


ans = solv(14, 5000)
print(ans)


def search(i, j):
    "求解路径"
    summer = 0
    while i >= 0 and j >= 0:
        if solv(i, j) == solv(i - 1, j - conduct[i]) + conduct[i]:
            print("index:" + str(i + 1) + "  weight:" + str(conduct[i]))
            j -= conduct[i]
        i -= 1


search(14, 5000)
