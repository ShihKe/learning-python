# -*- coding: utf-8 -*- 
# sorted 可对list进行排序，可映射一个key函数来自定义排序
ex_l = sorted ( [23, 45, -44, -2] , key = abs)
print (list (ex_l))

L = [ ('bob',65), ('Adm',84), ('Bart',93), ('Lisa',33)]
def by_name(t):
    return t[0].lower()
L1 = sorted (L, key = by_name)
print (L1)
def by_score(t):
    return -t[1]  #"-"待ing
L2 = sorted ( L, key = by_score)
print (L2)
