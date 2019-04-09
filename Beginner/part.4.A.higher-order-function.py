# -*- coding:utf-8 -*-
#higher-order-function
#变量可以指向函数
f = abs
print ( f(-19) )
# 函数名也是变量
# 传入函数，一个函数可以接收另一个函数作为参数（高阶函数）
def add(x, y, fun):
    return fun(x) + fun(y)

print(add(-5, -16, abs))
