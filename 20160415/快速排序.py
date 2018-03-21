# coding:utf-8


def sort(L):
    if not L: return []
    else:
        return sort([x for x in L[1:] if x < L[0]]) + L[0:1] + sort([x for x in L[1:] if x >= L[0]])