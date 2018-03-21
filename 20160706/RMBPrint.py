# coding:utf-8
"""
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示.
注意：请以Unicode的形式输出答案。你可以通过decode("utf8")来将utf8格式的字符串解码为Unicode，例如你要输出ans = "零圆", print ans.decode("utf8").
Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
"""


num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit = ['亿', '万', '仟', '佰', '拾', '']
baseList = [100000000, 10000, 1000, 100, 10, 1, 0]
def rmb(money):
    L = []
    level = 0
    while baseList[level] > money: level += 1
    base = baseList[level]
    if base <= 1:
        L.append(num[money])
    else:
        L.extend(rmb(money // base))
        L.append(unit[level])
        r = money % base
        if r:
            if r * 10 < base: L.append(num[0])
            L.extend(rmb(r))
    return L

a = 103
L = []
if a < 0:
    L.append('负')
    a = -a

L.extend(rmb(a))
L.append('圆')

print ''.join(L).decode("utf8")
