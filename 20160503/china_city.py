# coding:utf-8
"""
解析“中国最新省市区县大全”
"""
import xlrd


def open_excel(path, table_name):
    try:
        data = xlrd.open_workbook(path)
        table = data.sheet_by_name(table_name)
        # print 'open excel success'
        return table
    except Exception, e:
        print 'open excel failed!'
        print str(e)

def add_tree():
    province_city = {}
    city_county = {}
    table = open_excel(u'D:\迅雷下载\中国最新省市区县大全.xls','Sheet2')

    # provinces = table.col_values(0, 2)
    # cities = table.col_values(2, 2)
    index = 2
    for province in table.col_values(0, 2):
        if province:
            province_city[province] = []  # 记录省信息
            p_index = index  # 记录某省开始的行数
            county_num = 0
            for city in table.col_values(2, p_index):  # 从省开始的行数遍历市列表
                c_index = p_index + county_num  # 市开始的行数=省开始的行数+县的个数
                if table.col_values(2, c_index):  #
                    province_city[province].append(city)
                    city_county[city] = []
                    county_num = int(table.col_values(1, c_index, c_index+1)[0])
                    # county_num = int(county_num)
                    for county in table.col_values(3, c_index, c_index+county_num):
                        city_county[city].append(county)
                    c_index += county_num
                else:
                    continue
            index += 1
        else:
            index += 1


    for i in province_city.keys():
        for j in province_city[i]:
            print i,':',j
    print "_______________________________"
    for i in city_county.keys():
        for j in city_county[i]:
            print i, ':', j

add_tree()
