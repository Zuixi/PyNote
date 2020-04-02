#-*-coding=utf-8-*-

# 简单的一个类实例
class Ta():
    var1 = 'demo'
    var2 = 'test'

    def fun():
        print('简单测试类方法')
    
# 使用类的方法和属性
print(Ta.var1)
Ta.fun()

# 在同一个类里，方法如何调用类属性
class Demo():
    var1 = '被调用'

    # 在这里是有使用classmethod和cls才能调用类属性，缺一不可，不然会报错
    @classmethod
    def useAttributeInClass(cls):
        print(cls.var1)

    @classmethod
    def receivePatameters(cls, value):
        print('use value {} in the class'.format(cls.var1))
        print('received a parameter, it is {}'.format(value))

# 测试Demo类的方法
Demo.receivePatameters(123)

# 对于类属性的修改
class ModifyValue():
    value = 0

    @classmethod
    def modifyvalue(cls):
        print('current value is {}'.format(cls.value))
        cls.value = input('enter your number:')
        print('after modifide value, it is {}'.format(cls.value))


# 测试是否能够修改
m = ModifyValue()
m.modifyvalue()

# 类的构造函数和析构函数
# __init__
# __del__

class TestDelAndInit(object):
    
    def __del__(self):
        print('destroy success')
    
    def __init__(self,str):
        print('with parameter {} init success'.format(str))
    
# 测试析构函数和构造函数
t1 = TestDelAndInit('hello')
del t1


# 类的继承和多态
"""
1. 在定义类时，可以在()里写上继承的类名字，如果不需要继承类的话最好写上object
2. python支持多继承
3. 如果父类中含有相同方法名，并且子类中没有指定，则是按照从左到右的顺序
4. 继承的作用
    * 继承父类的方法和属性
    * 可以覆盖父类的属性和方法
"""

class Shape(object):
    var =  object()

    "构造函数"
    def __init__(self,name):
        self.name = name
    
    "返回面积"
    def getArea(self):
        pass

    " 返回周长"
    def getC(self):
        pass

    "显示对象的信息"
    def display(self):
        pass

    "一个默认函数，不做任何事"
    def doNothing(self):
        print('Shape do nothing with object {}'.format(self.var))

    "显示当前是哪个类"
    def OutInfo(self):
        print('Hello,this is shape called {}'.format(self.name))

class Rectangle(Shape):
    # 定义一个类成员
    var = 'rectangle'

    "构造函数"
    def __init__(self,width,height,name):
        # 父类构造函数的调用
        super(Rectangle,self).__init__(name)
        self.width = width 
        self.height = height
    
    "获取Width"
    @property
    def getWidth(self):
        return self.width

    @property
    def getHeight(self):
        return self.height
    
    "重写面积函数"
    def getArea(self):
        return self.width * self.height

    "重写周长函数"
    def getC(self):
        return 2 * ( self.width + self.height)

    "在这里重写display必须加上self,不然在对象调用这个方法的时候会出现类型错"
    def display(self):
        print('this is Rectangle')

    "使用类的成员变量"
    def showvar(cls):
        print('value of Rectangle is {}'.format(cls.var))

    "多态函数的实现"
    def OutInfo(self):
        print('Hello,this is a shape called {}'.format(self.name))

# 测试Rectangle的方法和属性
r = Rectangle(12,19,'Rectangle')
print(type(r))
# 调用重载的方法
r.display()
# 调用父类的方法
r.doNothing()
# 调用计算面积函数
print('Area of r is {}'.format(r.getArea()))
r.showvar()
print('value of Rectangle is {}'.format(r.var))

"多态函数的实现"
def OutInfoOfShape(shape):
    shape.OutInfo()

# 测试多态函数是否成功
OutInfoOfShape(Shape('Basic'))
OutInfoOfShape(r)

    

