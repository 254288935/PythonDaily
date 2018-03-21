# coding:utf-8
"""
解析跟进表.xlsx
[name, email, phone_number, current_employer, current-title]
"""
import xlrd

def open_excel(path=None, table_name=None):
    try:
        data = xlrd.open_workbook(path)
        table = data.sheet_by_name(table_name)
        return table
    except Exception, e:
        print str(e)


# [name, email, phone_number, current_employer, current-title]
def demo():
    table = open_excel(u'D:\跟进表.xlsx', u'Goyoo')


if __name__ == "__main__":
    table = open_excel(u'D:\跟进表.xlsx', u'Goyoo')
    # for i in table.row_values(0):
    #     print i
    print     table.row_values(0).index(u"联系人")


