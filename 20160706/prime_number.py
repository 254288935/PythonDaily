# coding:utf-8
"""
第2333个能被2或者被3整除的正整数是多少?
"""


def foo1():
    result_list = []
    for i in range(1,10000):
        if i%2==0 or i%3==0:
            result_list.append(i)

    if result_list[2333]:
        print result_list[2333]
    return result_list

def foo2():
    result_list = []
    i = 0
    while not result_list[2333]:
        i+=1
        if i%2 == 0 or i%3 == 0:
            result_list.extend(i)
    print result_list

def foo3(index):
    quotient, reminder = divmod(index, 4)
    addend_dic = {1:2, 2:3, 3:4}
    return quotient*6 + addend_dic[reminder]

if __name__ == "__main__":
    # print foo1()

    # for i in range(5000):
    #     print i,
    #     if i % 6 == 0:
    #         print '\n',

    # for i in range(1,4999):
    #     if i % 6 == 0:
    #         print i
    #     else:
    #         print i,

    print foo3(2333)
