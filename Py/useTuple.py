#-*-coding:utf-8-*-
#---Tuple的使用---

number = [123, 12232]
tupleSample = ('Alex', 'Apple', 'Amazon', 124, number)
 
print(tupleSample)
 
# 修改numberl里的值
number[0], number[1] = 12, 14
print(tupleSample)

# 英雄名字
name = ('李白', '韩信', '猴子')
# 英雄特性
skill = ('免疫', '突进', '爆发')

list1 = [1,2,3,4,5]

# 计算tuple个数
print(len(name))

# 连接，tuple相加
print(name + skill)

# 复制tuple
print(name * 3)

# 将list 转化为 tuple
print(tuple(list1))

# 判断元素是否在tuple中
print('韩信' in name)