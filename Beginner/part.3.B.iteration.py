# -*- coding: utf-8 -*-
# iteration: 任何数据类型可通过for....in 进行迭代
# test 查找list中的最大 最小值

def findMinAndMax (L):
    min = L[0]
    max = L[0]
    if L == []:
        return (None,None)
    else:
        for i in L:
            if i < min:
                min = i
            elif i > max :
                max = i
    return (min,max)

L = [1, 2, 3, 4, 5]
print (findMinAndMax(L))

# 像C一样的带下标的for循环:
for i, value in enumerate (['shih','shi','scy','s','c','y']):
        print (i,value)


#判断对象是否可迭代：collections
from collections import Iterable
print ( isinstance('aaa', Iterable) )
print ( isinstance([1,2,3,], Iterable) )
print ( isinstance(123, Iterable) )
