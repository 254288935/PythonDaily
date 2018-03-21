# coding:utf-8
"""
发红包
"""


family_tree = {}
family_exist = []


def add_family(pFather,pSon):
    if not(pFather and pSon):
        return -1
    # 初次添加成员
    if not family_tree:
        family_tree[pFather] = {'father': None, 'son': [pSon]}
        family_tree[pSon] = {'father': pFather, 'son': []}
        family_exist.append(pFather)
        family_exist.append(pSon)
        return 0
    if pFather in family_exist:
        if len(family_tree[pFather]['son']) > 10:
            return -1
        if pSon in family_tree[pFather]['son']:
            return -1
        family_tree[pFather]['son'].append(pSon)
        family_tree[pSon] = {'father': pFather, 'son': []}
        family_exist.append(pSon)
        return 0
    return -1


def cal_money(pFamilyMember):
    if pFamilyMember in family_exist:
        money = len(family_tree[pFamilyMember]['son']) * 100
        for i in family_tree[pFamilyMember]['son']:
            money += cal_money(i)
        return money
    return -1


def clear():
    family_tree.clear()
    global family_exist
    family_exist = []
    return


print(add_family('zhao1', 'qian1'), 0)
print(add_family('zhao1', 'qian2'), 0)
print(add_family('zhao1', 'qian3'), 0)
print(add_family('qian1', 'sun1'), 0)
print(add_family('qian1', 'sun2'), 0)
print(add_family('sun2', 'li5'), 0)
print(add_family('qian2', 'sun3'), 0)
print(add_family('qian3', 'sun4'), 0)
print(add_family('qian3', 'sun5'), 0)
print(add_family('sun4', 'li1'), 0)
print(add_family('sun4', 'li2'), 0)
print(add_family('sun4', 'li3'), 0)
print(add_family('sun5', 'li4'), 0)
print(cal_money('qian3'), 600)
print(cal_money('li1'), 0)
print(cal_money('zhao1'), 1300)
print(cal_money('wang5'), -1)
clear()