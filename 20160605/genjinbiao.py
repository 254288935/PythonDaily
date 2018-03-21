# coding:utf-8
"""
读取跟进表的关键信息
联系人 手机 邮箱 公司 title 备注
{name:[phone_number, email, company, title, remark], name:[phone_number, email, company, title, remark]}
C:\Users\stephen\Desktop\跟进表.xlsx 忆恒创源
"""
import xlrd


def open_excel_sheet(excel_path, sheet_name):
    # name = sheet_name.decode('utf-8')
    excel_path = excel_path.decode('utf-8')
    try:
        workbook = xlrd.open_workbook(excel_path)
        sheet = workbook.sheet_by_name(sheet_name)
        print 'open succeed '
        return sheet
    except Exception, e:
        print 'open failed:', str(e)


def parse_sheet():
    """
    {name:[phone_number, email, company, title, remark], name:[phone_number, email, company, title, remark]}
    """
    sheet = open_excel_sheet(r'C:\Users\stephen\Desktop\跟进表.xlsx', u'京东金融')
    # 找到信息列列号
    cols = sheet.row_values(0)
    name_index = cols.index(u'联系人')
    phone_index = cols.index(u'手机')
    email_index = cols.index(u'邮箱')
    company_index = cols.index(u'公司')
    title_index = cols.index('title')
    remark_index = cols.index(u'补充说明')
    # 读取信息

    contact_person = {}
    index = 1
    for name in sheet.col_values(name_index, 1):
        if name:
            contact_person[name] = []
            person_info = sheet.row_values(index)
            contact_person[name].append(str(person_info[phone_index]))
            contact_person[name].append(person_info[email_index])
            contact_person[name].append(person_info[company_index])
            contact_person[name].append(person_info[title_index])
            contact_person[name].append(person_info[remark_index])
            index += 1
        elif '' == name:
            print 'blank row'

    return contact_person

if __name__ == '__main__':
    data = parse_sheet()
    print data




















