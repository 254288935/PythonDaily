# coding:utf-8
"""
冒泡排序
"""

import random
def bubblesort(a):
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if a[j] < a[i]:
                a[j],a[i] = a[i],a[j]

def Test():
    a = []
    for i in range(1,10):
        a.append(random.randint(1,100))
    print("orginal: ",a)
    #print "after sort: "
    bubblesort(a)
    print("after sort:",a)

if __name__ == '__main__':
    Test()