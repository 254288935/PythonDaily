# coding:utf-8
"""
三种不同方法求最大子序列和
"""


def maxsum_of_sublist1(input_list):  # 第一种实现方法
    cursum = maxsum = input_list[0]
    i = 1
    while i < len(input_list):
        if cursum <= 0:
            cursum = input_list[i]
        else:
            cursum += input_list[i]

        if cursum > maxsum:
            maxsum = cursum

        i += 1

    return maxsum


def maxsum_of_sublist2(input_list):  # 第二种实现方法
    cursum = maxsum = 0
    for i in input_list:
        cursum += i
        if cursum > maxsum:
            maxsum = cursum
        elif cursum < 0:
            cursum = 0
    return maxsum


def maxsum_of_sublist3(a):   # 第三种实现方式
    currSum = 0
    mSum = 0

    for i in range(0, len(a)):
        for j in range(i, len(a)):
            currSum = 0
            for k in a[i:j]:
                currSum += k
            if currSum > mSum:
                mSum = currSum
    return mSum


print(maxsum_of_sublist1([6, 2, -3, -5, 9, -5, 8, -7, -6, 4, 2]))
print(maxsum_of_sublist2([6, 2, -3, -5, 9, -5, 8, -7, -6, 4, 2]))
print(maxsum_of_sublist3([6, 2, -3, -5, 9, -5, 8, -7, -6, 4, 2]))
