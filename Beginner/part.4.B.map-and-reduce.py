# -*- coding:utf-8 -*-
# map(function,Iterable),一次接收Itetable的每个元素，并返回new Iterator
def Ex_f (x):
    return x * x
ex = [1, 3, 4]
ex_r = map ( Ex_f,ex )
print (list(ex_r))

'''for i in ex_r:
    print (i)
 '''
 # reduce(function, Iterable)/,必须接收2个参数，把结果继续和序列下一个元素累积
from functools import reduce
def add (x, y):
    return x + y
ex_sum =  reduce (add,[1,3,4,5,6])
print (ex_sum)
# test1
def normalize(Name):
    NameL = Name[0].upper() + Name[1:].lower()
    return NameL
name = ['adma', 'LIDA', 'barT']
print ( list (map (normalize,name)))

#tese2
def prod(Q):
    def ji(x, y):
        return x * y
    return reduce (ji,Q)
ex_num = [2, 4, 5, 6, 2]
print (prod(ex_num))

# test3
def str2float(s):
    for i in range( len(s)):
        if s[i] == '.':
            break
    L = s[:i] + s[i+1:]
    m = len(s) -i -1
    di = { '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    def char2num(s):
        return di[s]
    def f(x,y):
        return x * 10 + y
    return reduce(f,map(char2num,L))/10**m
print (str2float('123.33'))









