# -*- coding: utf-8 -*- 
# generator 用yield 区别于普通函数，遇到yield暂停，用next（）是继续执行yield下一个语句
def fib (max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b #是tuple 用于交换数值，在C中需要变量temp
        n = n + 1
    return "done"

print (fib (6))

for i in fib(6):
    print (i)

g = fib (6)
while True:
    try:
        x = next (g)
        print ('g:',x)
    except StopIteration as e:
        print ('Genetator return value:', e.value)
        break


# test
def triangles ():
    L = [1]
    S = []
    while 1:
        yield L     #到此为止，下一次循环从下一个语句开始
        L = [1] + S + [1]
        S = []
        for i in range (len (L) - 1 ):
            S.append(L[i] + L[i + 1 ])

t = triangles ()
for x in t:
    print (x)
