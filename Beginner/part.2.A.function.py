# !/usr/bin/python
# -*- coding:UTF-8 -*-
# 调用函数：
a  = -111
print ('abs= %f' % a)

#定义函数：def (x):  retrun x 
import math
def quadratic (a, b, c):
    if a != 0 :
        der =(b*b-4*a*c)  
        if der >= 0:
            x1 = (-b + math.sqrt(der) ) / 2*a
            x2 = (-b - math.sqrt (der)) / 2*a
            print ('x1=: %f' % x1)
            print ('x2=: %f' % x2)
            return 
        else : 
            der < 0
            print ('没有实数根')
            return
    else :
        print ('a 不能为0')
        return
quadratic (1,3,5)

#函数参数：
# #位置参数：按顺序依次赋值：

def power (x, n):
    s = 1
    i = 0
    while i < n:
        i = i + 1
        s = x * s
    return s

print (power (4,4))

#默认参数：
def power1 (x, n=2):
    s = 1
    i = 0
    while i < n:
        i = i + 1
        s = s * x
    return s

print (power1 (3))

#k可变参数：参数个数不确定(tuple or list):
def calc (*num):
    sum = 0
    for i in num:
        sum = sum + i * i 
    return sum

print (calc(5, 1, 2))
# # 调用tuple or lisr :
l = [2, 4, 5]
print (calc(*l))
# 关键字参数 （dict）：
def key_person(name,age,**kw):
    print ('name: ',name, 'age: ',age, 'other: ', kw)

key_person('shi', 23, city='kunming', job='stu')
# #调用dict:
dict = {'city':'bingjin', 'gender':'F'}
print ( key_person('scy',32,**dict) )

# 命名关键字参数:
# #只接手**作为关键字参数,调用时要包含关键字：
def dict (name, age, *, city, job) :
    print ('name: ',name, 'age: ',age, 'city: ',city, 'job: ',job)

print (dict('shih', 23, city='yuxi',job='stu'))

# #包含 **时，就不用在命名关键词前用*

#参数组合：定义顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数


#递归 在函数内部调用函数自身（注意栈溢出）
def foctrial (n):
    if n == 1 :
        return 1
    return n * foctrial( n-1 )

print ( foctrial(5) )
#tail recursion
