# coding:utf-8
"""
删除重复元素的几种方法
"""

def del_repeat1(input_list):
    for i in input_list:
        if input_list.count(i) > 1:
            input_list.remove(i)
    return input_list

def del_repeat2(input_list):
    return set(input_list)

print(del_repeat1(list('hello buddy')))
print(del_repeat2(list('hello buddy')))