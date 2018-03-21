# coding:utf_8
"""
用selenium操作rightfit页面，实现表单的输入
"""
import selenium
from selenium import webdriver
import time
import xlrd
from selenium.webdriver.common.keys import Keys  #需要引入keys包


# 登陆rightfit
def work(browser):
    url = "https://cn.rightfit.it/index.php"
    browser.get(url)
    try:
        # 输入账号和密码
        browser.find_element_by_name("username").send_keys(u"zquan@china.comrise.com")
        browser.find_element_by_name("password").send_keys("611733")
        time.sleep(2)

        #点击按钮提交登录表单
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

    index = 1
    while info_of_row(index):
        # if r"https://cn.rightfit.it/cn_upload/coldCall.php" == browser.current_url:
        fill_blank(browser, index)

        index += 1


#　打开表格
def open_excel(path=None, table_name=None):
    try:
        data = xlrd.open_workbook(path)
        table = data.sheet_by_name(table_name)
        return table
    except Exception, e:
        print "open excel fail:", str(e)

#　读取excel表格一行内容，行由index指定
def info_of_row(index):
    table = open_excel(u'D:\跟进表.xlsx', u'Sheet1')
    # [name, email, phone_number, current_employer, current_title]
    # name_index = table.row_values(0).index(u"联系人")
    # email_index = table.row_values(0).index(u"邮箱")
    # phone_number_index = table.row_values(0).index(u"手机")
    # current_employer_index = table.row_values(0).index(u"公司")
    # current_title_index = table.row_values(0).index(u"title")
    person_info = []
    for info in table.row_values(index):
        person_info.append(info)
    # print person_info
    return person_info

# 将读取到的人员信息填写到网页表单中
def fill_blank(browser, index):
    table = open_excel(u'D:\跟进表.xlsx', u'Sheet1')
    info = table.row_values(index)
    # print info[0],info[1],info[2]
    browser.find_element_by_name("firstName").send_keys(info[0])
    time.sleep(.5)
    browser.find_element_by_name("lastName").send_keys(info[0])
    time.sleep(.5)
    browser.find_element_by_name("email").send_keys(info[1])
    time.sleep(.5)
    browser.find_element_by_name("phone").send_keys(str(int(info[2])))
    time.sleep(.5)
    browser.find_element_by_name("currentEmployer").send_keys(info[3])
    time.sleep(.5)
    browser.find_element_by_name("currentTitle").send_keys(info[4])
    time.sleep(.5)
    browser.find_element_by_name("countries").send_keys('c')
    browser.find_element_by_name("countries").send_keys(Keys.ENTER)
    time.sleep(.5)
    browser.find_element_by_name("source").send_keys('l')
    browser.find_element_by_name("source").send_keys(Keys.ENTER)
    time.sleep(.5)
    browser.find_element_by_name("action").click()
    time.sleep(5)



if __name__ == "__main__":
    browser = webdriver.Firefox()
    work(browser)
    # print info_of_row(1)
    # info = info_of_row(1)
    # print info[0],info[1],int(info[2])
