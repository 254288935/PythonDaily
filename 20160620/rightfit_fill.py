# coding:utf_8
"""
用selenium操作rightfit页面，实现表单的输入
"""
import selenium
from selenium import webdriver
import time
import xlrd
from selenium.webdriver.common.keys import Keys  # 需要引入keys包


# 登陆rightfit
def work(browser):
    url = "https://cn.rightfit.it/index.php"
    browser.get(url)
    try:
        # 输入账号和密码
        browser.find_element_by_name("username").send_keys(u"zquan@china.comrise.com")
        browser.find_element_by_name("password").send_keys("611733")
        time.sleep(2)

        # 点击按钮提交登录表单
        browser.find_element_by_name("action").click()
        time.sleep(5)

        # 验证登录成功的url
        currUrl = browser.current_url
        if currUrl == "https://cn.rightfit.it/index.php":
            print u"open web success"
        else:
            print u"open web failure"
        print u"点击cold call"
        try:
            browser.get(r"https://cn.rightfit.it/cn_upload/coldCall.php")
            time.sleep(3)
        except Exception, e:
            print str(e)
            print u"点击cold call 失败"
    except:
        print u"open web failure"

    # if r"https://cn.rightfit.it/cn_upload/coldCall.php" == browser.current_url:
    fill_blank(browser)


# 打开表格
def open_excel(path=None, table_name=None):
    path = path.decode('utf-8')
    try:
        data = xlrd.open_workbook(path)
        table = data.sheet_by_name(table_name)
        return table
    except Exception, e:
        print "open excel fail:", str(e)


# 读取excel表格一行内容，行由index指定
def parse_sheet():
    """
    {name:[phone_number, email, company, title, remark], name:[phone_number, email, company, title, remark]}
    """
    print '==================start parse sheet=================='
    sheet = open_excel(r'C:\Users\stephen\Desktop\跟进表.xlsx', u'Sheet1')
    # 找到信息列列号
    cols = sheet.row_values(0)
    name_index = cols.index(u'联系人')
    phone_index = cols.index(u'手机')
    email_index = cols.index(u'邮箱')
    company_index = cols.index(u'公司')
    title_index = cols.index('title')
    remark_index = cols.index(u'部门')
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
    print '================== parse sheet finish=================='
    return contact_person


# 将读取到的人员信息填写到网页表单中
def fill_blank(browser):
    info = parse_sheet()
    print '==================start fill in=================='
    for key in info.keys():
        browser.find_element_by_name("firstName").send_keys(key)
        time.sleep(.5)
        browser.find_element_by_name("lastName").send_keys(key)
        time.sleep(.5)
        browser.find_element_by_name("email").send_keys(info[key][1])
        time.sleep(.5)
        browser.find_element_by_name("phone").send_keys(info[key][0].replace('.0', ''))
        time.sleep(.5)
        browser.find_element_by_name("currentEmployer").send_keys(info[key][2])
        time.sleep(.5)
        browser.find_element_by_name("currentTitle").send_keys(info[key][3])
        time.sleep(.5)
        browser.find_element_by_name("countries").send_keys('c')
        browser.find_element_by_name("countries").send_keys(Keys.ENTER)
        time.sleep(.5)
        browser.find_element_by_name("source").send_keys('l')
        browser.find_element_by_name("source").send_keys(Keys.ENTER)
        time.sleep(1)
        browser.find_element_by_name("action").click()
        time.sleep(5)


if __name__ == "__main__":
    browser = webdriver.Chrome()
    work(browser)
    # info = parse_sheet()
    # for key in info.keys():
    #     print info[key]
