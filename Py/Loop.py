#-*-coding=utf-8-*-
# use loop in python

# break 
# continue
# pass 空语句，保持结构完整性

# for loop
print('for loop eaxmplify--->')
# string
for letter in 'hello':
    print(letter,end=' ')

print()

# list
for itr in [1,2,3,4]:
    print(itr,end=' ')

print()

# dict
dict1 = {'李白':'刺客', '韩信':'刺客', '不知火舞':'法师'}
for itr in dict1:
    print(itr, end=' ')
print()

# set
set1 = set([23,12,5])
for itr in set1:
    print(itr, end=' ')
print()

# int is not working ,it is not a iterable
#for itr in 100:
#    print(itr)

# 使用range函数控制循环次数
for i in range(3):
    print(i, end=' ')
print()

for i in range(4,9,2):
    print(i, end=' ')
print()

for i in range(4,9):
    print(i, end=' ')
print()

print('while loop beginning---->')

# 实现从1到100的累加
sum = 0
count = 0
while (count <= 100):
    sum += count
    count = count + 1
print(sum)

# 判断10到30有几个合数和质数
# 这里使用for else，其实也还有while else
for num in range(10,31):
    for i in range(2, num):

        if (num % i == 0):
            j = num / i
            print('%d 是一个合数' %num)
            break

    else:
        print('%d 是一个质数' %num)


# 打印乘法表
for out in range(1,10):
    for inner in range(1,out + 1):
        print('{} * {} = {}\t'.format(out, inner, out * inner), end=' ')
    print()
