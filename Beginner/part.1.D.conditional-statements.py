# -*- coding: utf-8 -*-
# if elif else 注意缩进（语句块）
# exercise :
H = input('height: ')
height = float (H)
W = input ('weight:')
weight = float (W)
BMI = weight/(height*height)
if BMI <25:
    print("过轻")
elif 18.5 <= BMI < 25:
    print("正常")
elif 25 <= BMI < 28:
    print("过重")
elif 28 <= BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")
