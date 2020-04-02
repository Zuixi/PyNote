#-*-coding:utf-8-*-
# ---use set-----


sample = set([1,32,12])
print(sample)
sample.add(123)
print(sample)
sample.add(123)
print(sample)

sample.remove(32)
print(sample)

set1 = set([1,3,4,5,6,7,9])
set2 = set([2,3,4,5])
print(set1)
print(set2)

# 求两个set的交集
print(set1 & set2)

# 求两个set的并集
print(set1 | set2)

# 求两个set的差集
print(set1 - set2)
print(set2 - set1)

# 利用set去重
listsample = [1,2,1,1,2,32,1,2,3,5]
print(set(listsample))