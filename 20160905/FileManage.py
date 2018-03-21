# coding:utf-8
"""
这里需要将这些垃圾归类，并计算其大小，之后根据用户需求删除或继续保留。
这里有一个文件夹，答案就在里面最大的text文档里面。
"""
import os
PATH = u'D:\\root'

def file_manage():
    size = 0
    answer_path = ''
    for parent,dirnames,filenames in os.walk(PATH):
        for i in filenames:
            path = os.path.join(parent, i)
            if os.path.getsize(path) > size:
                size = os.path.getsize(path)
                answer_path = path
    print answer_path


if __name__ == '__main__':
    file_manage()