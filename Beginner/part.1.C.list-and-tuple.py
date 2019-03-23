# -*coding: utf-8 -*-

#list 定义list E.g:
classmater = ['shih', 'scy', 'shihke']
print (classmater)

#用引索访问元素
print (classmater[0])
print (classmater[1])
#len()查看元素
len(classmater)

#追加元素
classmater.append('chang')
print (classmater)
classmater.insert(0,'you')
print (classmater)
#删除元素
classmater.pop()
print (classmater)
classmater.pop(0)
print (classmater)

#替换元素
classmater[0] = 'sscc'
print (classmater)
#list中可以有不同的数据类型 E.g: L = ['shi',123, True]

#二维数组，（多维）
i= ['python', 'java', ['asp','c']]
print(i)
print(i[2][1])


# tuple 元组，初始化后不能修改
classmater = ('sss', 'ccc', 'yyy')
print (classmater)
print (classmater[2])
# #元组只有一个元素用 ' E.g
t = (1,)
print (t)
#tuple 中有list list可修改


#list tuple 都可以空
