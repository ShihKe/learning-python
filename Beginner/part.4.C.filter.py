# -*- coding: utf-8 -*-
# filter 像map一样一次读取元素并返回Iterator，过滤掉false
def is_odd(n):
    return n % 2 == 1
Li = range(11)
ex_l = list (filter(is_odd, Li))
print (ex_l)

def not_empty(S):
    return S and S.strip() #去首的空格，没有去掉尾的（?）

string = ['','a', ' b','c ',None ,' ','f']
print (list (filter (not_empty, string)))

#test1 求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)
    return it
for n in primes():
    if n < 1000:
        print(n)

    else:
        break


#test 2
#plindromic number







