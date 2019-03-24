
# -*- coding: utf-8 -*-
# dict:key-value:
d = {'shih':95, 'scy':85, 'shihke':75}
print (d)
print(['shih'])
d ['you'] =55
print (d)
d['you'] = 75
print (d)
# 用in 判断key是否存在：
'shi' in d
# get ()判断，若不存在可以指定：
d.get('shi')
d.get("shi",75)
#pop(key)删除key
d.pop('shih')
print(d)


#set key的集合，在set中没有重复的key，可作交集、并集
s = set([1, 3, 2])
print (s)
s.add (2)
print (s)
s.add (4)
print (s)
s.remove (1)
print (s)

# 数学上的交集 并集:
s1 = set([12,13,14])
s2 = set([12,14,15])
j = s1 & s2
B = s1 | s2
print (j)
print(B)
# set dict 都是不可变对象
