# !/usr/bin/python3
# -*- coding:utf-8 -*-
# class 类和实例 访问限制 继承和多态 获取对象信息 实例属性和类属性
# test 1 
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        print( self.__gender )
    def set_gender(self, gender):
        if gender == 'male':
            print ('male')
        elif gender == 'female':
            print ('female')
        else :
            print ('enter True genter')

stu = Student('shih','male')
stu.get_gender()
stu.set_gender('female')
