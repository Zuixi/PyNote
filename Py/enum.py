# -*- coding = utf-8 -*-

from enum import Enum, unique

"""
枚举类的使用

"""
# Enum中第一个参数是枚举类的类名，第二个参数是枚举类的值
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr'))

# 遍历枚举类型，遍历枚举类使用__members__方法，member.value默认从1开始
for name, member in Month.__members__.items():
    print(name,'-----------------', member, '-----------------',member.value)

# 直接使用一个枚举变量
print(Month.Jan)
print(Month)

"""
自定义类型的枚举
通过Enum派生类来实现
"""

"@unique可以确保没有重复值"
@unique
class CMonth(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Api = 'April'
    May = 'May'

if __name__ == "__main__":
    print(CMonth.Jan,'-----------',CMonth.Jan.name, '-----------------',CMonth.Jan.value)

    # 遍历CMoth的枚举值
    for name, member in CMonth.__members__.items():
        print(name,'--------',member,'-------------',member.value)

# 枚举类的比较
"""
枚举变量无序
"""

class Demo(Enum):
    A = 12
    B = 2
    C = 1

_brand_a = Demo.A
_brand_b = Demo.B
_brand_c = Demo.C

# 测试枚举变量的比较
# 注意is和==的区别
print('_brand_a == 12 ->  {}, _brand_a == Demo.A-->{}'.format(_brand_a == 12, _brand_a == Demo.A))
print('_brand_a is 12 ->  {}, _brand_a is Demo.A-->{}'.format(_brand_a is 12, _brand_a is Demo.A))

"""
Enum的类是不支持变量之间进行大小比较的
如果需要进行大小比较，则需要使用IntEnum类
"""