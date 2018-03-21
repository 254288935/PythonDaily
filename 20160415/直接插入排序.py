# coding:utf-8
"""
直接插入排序
"""

# -*- coding: utf-8 -*-
import random,time
r = random.Random()

li = [r.randint(1,300) for i in range(20)]  #生成随机数

print(li)
print("-"*30)

start_time = time.time()

for i in range(len(li)):
    temp = li[i]
    j = i
    while j > 0 and temp < li[j-1]:
        li[j] = li[j-1]
        j -= 1
    li[j] = temp

print(li)

end_time = time.time()

print(end_time - start_time)