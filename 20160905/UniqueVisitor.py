# coding:utf-8
"""
每一个网站都会根据访客日志统计访客数据，比如UV（Unique Visitor，即访问用户）。
UV能够回答一个关键的市场营销问题：“到底有多少人（潜在客户）看到了你发布的信息（即网站）”。
这道题的任务是根据给出的某购物网站访问日志，统计当天该网站UV。
日志文件的每一行代表一次访问行为，每行分别包含三项，以空格分隔，格式为：
用户访问的时间 用户的id 用户的行为
请问8月24号当天，该网站有多少个用户（相同用户id算一个用户）访问？
"""
import time


PATH = u'D:\\迅雷下载\\uv.txt'


def get_uv_count():
    UV_file = open(PATH, mode='r')
    UVList = [lines.split(' ') for lines in UV_file.readlines()]
    IdList = []
    for record in UVList:
        if record[1] not in IdList:
            IdList.append(record[1])
    print len(IdList)


def get_uv_count2():
    UV_file = open(PATH, mode='r')
    UVList = [lines.split(' ')[1] for lines in UV_file.readlines()]
    print len(set(UVList))


def get_uv_count3():
    print len({i.split(' ')[1] for i in open(PATH)})


if __name__ == '__main__':
    time1 = time.clock()
    # get_uv_count()  # 47s
    # get_uv_count2()  # < 0.1s
    get_uv_count3()  # < 0.1s
    time2 = time.clock()
    print 'run time:', time2 - time1