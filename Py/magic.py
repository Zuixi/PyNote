# -*- coding=utf-8 -*-

class User(object):

    "使用magic method"

    "返回一个类的对象"
    def __new__(cls,*args,**kwargs):
        # 输出__new__方法的信息
        print('调用 def __new__ 方法')
        print(args)

        # 返回父类的方法
        return super(User,cls).__new__(cls)
    
    "对返回的对象赋值"
    def __init__(self, name, age):
        print('调用 __init__方法')
        self.name = name
        self.age = age

if __name__ == '__main__':
    usr = User('Helo', 123)

str