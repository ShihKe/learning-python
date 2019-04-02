# -*- coding: utf-8 -*-
#clice ,可对tulpe list string 进行clice
# E.g: l (a:b:n) a默认为l[0], b默认为[len(l)],n默认为1
l = list( range(100) )
print (l)
print ( l[:])
print (l[0:10])
print ( l[0:10:2] )
print ( l[-1:])
print ( l[:-1])
print ( l[:10])


# test
def trim(s):
    while s[:1] == ' ' :
        s = s[1:]
    while s[-1:] == ' ' :
        s = s[:-1]
    return s
m = ''
f = '  hello shis   ' 
print (trim(m))
print (trim(f))
