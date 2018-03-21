# coding:utf-8
"""
Python anydbm模块练习
"""


import dbm

def CreateData():
    try:
        db = dbm.open('db.txt', 'c')
        # key与value必须是字符串
        # db['int'] = 1
        # db['float'] = 2.3
        db['string'] = "I like python."
        db['key'] = 'value'
    finally:
        db.close()

def LoadData():
    db = dbm.open('db.txt', 'r')
    for item in db.items():
        print(item, '****')
    db.close()

if __name__ == '__main__':
    CreateData()
    LoadData()
