# string
slogan = 'never give up'
_itr_str = iter(slogan)

# list
fruits = ['apple', 'banana', 'strawbelly', 'grape']
_itr_list = iter(fruits)

# tuple
num = 1,2,3,4
_itr_tuple = iter(num)

# 使用for loop 便利迭代器对象
print(' use for loop to get element in itetator')
for var in num:
    print(var,end=' ')
else:
    print()

# 使用next()遍历迭代器对象
print('use next() to get element in iterator')
while True:
    try:
        print(next(_itr_list),end=' ')
    except StopIteration:
        break

gen = (x ** 3 for x in range(9))
print(type(gen))
print(gen)

while True:
    try:
        print(next(gen), end=' ')
    except StopIteration:
        break

# 以函数形式生成迭代器
def fun_gen():
    for i in range(9):
        print(i, end=' ')
fun_gen()

def gen_fun():
    for i in range(9):
        yield i
print(gen_fun())

# 斐波那契数列
def fib(n):
    a , b = 1, 1

    for i in range(n):
        yield a
        a , b = b, a + b
# use fib
for x in fib(10):
    print(x , end=' ')

# 杨辉三角
def triangle(n):
    L = [1]
    while True:
        yield L
        L.append(0)

        L = [L[i - 1] + L[i] for i in range(len(L))]

count = 0
for t in triangle(6):
    print(t)
    count = count + 1
    if (count == 6):
        break


