# -*- coding: utf-8 -*- 
# iterator： 可用于next()函数的对象都是iterator
#iterable 可用iter()函数获得iterator对象
# 判断 iterator itetable类型
from collections import Iterable
a = isinstance ( [] ,Iterable)
b = isinstance ( {} ,Iterable)
c = isinstance ( 'ac', Iterable)
d = isinstance ( 123 , Iterable)
print (a, b, c, d)

from collections import Iterator
A = isinstance ( [], Iterator)
B = isinstance ( {}, Iterator)
C = isinstance ( (x for i in range (10)) , Iterator)
print (A, B, C)

# python 中的for本质上就是不断调用next()函数
