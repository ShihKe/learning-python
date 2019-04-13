#-*- coding:utf-8 -*-
# partial 可加强函数
from functools import partial
int2 = partial( int, base = 2)
print ( int2 ('100000111') )
'''
相当于
kw = {'base':2}
int ('1000000111',**kw)
如果不指明 base = 2的话，那么2就作为*args的值
'''
#partial 可接收对象 *args **kw 三个参数


