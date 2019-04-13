# -*- coding:utf-8 -*-
# decorator 装饰器，在不影响函数结构的同事时扩展函数功能
from functools import wraps
def log (text):
    def decorator(func):
        def wraps(*args,**kwargs):
            print ('%s %s():'% (text,func.__name__))
            return func(*args,**kwargs)
        return wraps
    return decorator
@log('shih')
def now():
    print ('data')

now()
    
