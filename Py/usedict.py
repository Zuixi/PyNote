#-*-coding:utf-8-*-
#---dict的使用---

dict1 = {'李白':'刺客', '韩信':'刺客', '不知火舞':'法师'}
dict2 = {'abc':1234, 1234:'abc'}

print(dict1['李白'])

# 新增一个键值对
print(dict1)
# 最近新买了个英雄关羽，属性战士
dict1['关羽'] = '战士'
print(dict1)
#修改键值对
# 不知火舞还有一个属性是刺客，需要修改对应的属性
dict1['不知火舞'] = '法师&刺客'
print(dict1)

# 删除dict
# del可以删除dict中某个元素，也可以删除整个dict，clear方法可以清楚字典里的所有内容
# 关羽玩了很久都没学会，需要删掉这个键值对
del dict1['关羽']
print(dict1)

# 删除dict中所有元素
dict2.clear()
print(dict2)

# 删除dict
del dict2
