# -*- coding: utf-8 -*-
#Key words : loop; for...in, while; break, continue
#do...for :
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello,%s' % name)
#do...while:
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        print(n)
        sum = n + n
print('sum=: %d' % sum)

#break,continue,配合if使用，尽量少用
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

# berak:

