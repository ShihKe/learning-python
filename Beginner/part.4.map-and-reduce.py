# -*- coding:utf-8 -*-
# map()接收两个参数，一个函数一个iterable,一次作用到与序列的每个元素
def f(x):
    return x * x 
r = map( f, [1, 2, 3, 4, 5])
print(list (r) )

#str2itn
digits = {'0':0, '1':1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
from functools import reduce
def fn( x, y):
    return x * 10 + y
def char2num(s):
    return digits[s]
def str2int (s):
    return reduce ( fn, map (char2num,s))
print ( str2int('123444'))

#test
def normalize (name):
    L = name[0].upper() + name[1:].lower()
    return L

name = ['adam', 'LISA', 'barT']
na = map (normalize, name) 
print (list(na))
