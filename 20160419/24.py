#coding:utf-8


def isEqual(num1, num2):
    return abs(num1 - num2) < 1e-5;
# End of isEqual().

def expressionsFromExpOpSeq(expSeq, opSeq):
    assert(len(expSeq) == len(opSeq) + 1)
    if 1 == len(expSeq):
        yield expSeq[0]
        return
    # End of if.

    for idx in range(len(opSeq)):
        newExp = "(%s %s %s)" % (
            expSeq[idx], opSeq[idx], expSeq[idx+1])
        newExpSeq = expSeq[:idx] + [newExp] + expSeq[idx+2:]
        newOpSeq = opSeq[:idx] + opSeq[idx+1:]
        for exp in expressionsFromExpOpSeq(newExpSeq, newOpSeq):
            yield exp
    # End of for.
# End of expressionsFromExpOpSeq().

def expressionsFromExpSeq(expSeq):
    for opSeq in selections("+-*/", len(expSeq) - 1):
        for exp in expressionsFromExpOpSeq(expSeq, opSeq):
            yield exp
# End of expressionsFromExpSeq().

def expressions(numList):
    '''Generate expressions.
    '''
    if (0 == len(numList)): return;
    for numPerm in permutations(numList):
        expSeq = [str(n) for n in numPerm]
        for exp in expressionsFromExpSeq(expSeq):
            yield exp
# End of expressions().

numTuple=input("Please input 4 numbers to computer 24:(use ',' to divide them)")
numList=[float(i) for i in numTuple]
# numList = [1.0,4.0,5.0,6.0]
TARGET = 24.0
print("Your input is: %s" % numList)

for exp in expressions(numList):
    try:
        if isEqual(TARGET, eval(exp)):
            print("%s = %s" % (exp, TARGET))
    except ZeroDivisionError:
        pass
    # End of try.
# End of for.



#其中计算排列组合的代码来自Cookbook:



# Recipe 19.15. Generating Permutations, Combinations, and Selections

def _combinators(_handle, items, n):
    ''' factored-out common structure of all following combinators '''
    if n==0:
        yield [  ]
        return
    for i, item in enumerate(items):
        this_one = [ item ]
        for cc in _combinators(_handle, _handle(items, i), n-1):
            yield this_one + cc
def combinations(items, n):
    ''' take n distinct items, order matters '''
    def skipIthItem(items, i):
        return items[:i] + items[i+1:]
    return _combinators(skipIthItem, items, n)
def selections(items, n):
    ''' take n (not necessarily distinct) items, order matters '''
    def keepAllItems(items, i):
        return items
    return _combinators(keepAllItems, items, n)
def permutations(items):
    ''' take all items, order matters '''
    return combinations(items, len(items))


"""
示例:

Please input 4 numbers to computer 24:(use ',' to divide them)1,4,5,6
Your input is: [1.0, 4.0, 5.0, 6.0]
(4.0 / (1.0 - (5.0 / 6.0))) = 24.0
(6.0 / ((5.0 / 4.0) - 1.0)) = 24.0



也可以输入多个数字:

Please input 4 numbers to computer 24:(use ',' to divide them)2,3,4,5.5,6
Your input is: [2.0, 3.0, 4.0, 5.5, 6.0]
((2.0 - (3.0 / (4.0 - 5.5))) * 6.0) = 24.0
(2.0 * (3.0 - ((4.0 - 5.5) * 6.0))) = 24.0
((2.0 + (3.0 / (5.5 - 4.0))) * 6.0) = 24.0
"""