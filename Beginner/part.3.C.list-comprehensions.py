# -*- coding:utf-8 -*-
# list comprehensions :内置的创建list生成式
L = list (range(1,11))
j = [ x*x for x in range(1,11)]
print (L)
print (j)

# for 循环后还可以加上 if
J = [x * x for x in range(1 , 11) if x % 2 == 0 ]
print (J)

# 用list comprhensions 可以使代码简洁

#for 循环可以使用多个变量：
d = { 'x':'a', 'y':'b', 'z':'c'}
for k , v in d.items():
    print (k, '=', v)

#list comprhensions 也可以使用两个变量:
D = [k +  '=' +  v for k, v in d.items()]
print (D)

# test
T = ['Hello', 'World', 'IBM', 'Apple',12,13]
T1 = [ i.lower() for i in T if isinstance (i,str) == True]
T2 = [ x for x in T if isinstance (x,int) == True ]
T3 = [ s for s in T if isinstance (s,list) == True]
print (T1)
print (T2)
print (T3)

