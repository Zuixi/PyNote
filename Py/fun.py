
def sum(num1,num2):
    "两数之和"
    return num1 + num2

# 调用sum
print(sum(2,3))


# 返回多个参数
def division(num1,num2):
    "返回商和余数"
    return num1 // num2, num1 % num2
a, b = division(5,4)
print(a,b)
print(division(5,4))

def print_hero_info(name, attribute = '刺客'):
    # 输出英雄信息
    print('name = {} , attribute = {}'.format(name,attribute))

print_hero_info('李白')
print_hero_info('安琪拉','法师')

def print_info(a,b = None):
    print(b)
    if (b is None):
        b = []
    return b

def print_info1(a,b = []):
    print(b)
    return b

# test 两个默认值的不同之处
print('use None as default value---->')
result = print_info(1)
result.append('error')
print(result)

print('use [] as default value---->')
otherres = print_info1(1)
otherres.append('error')
print(otherres)

# 使用关键字参数
print_hero_info(attribute='战士', name='花木兰')
print_hero_info(name='猴子')


def out_info_hero(name, attribute, *, skill):
    # 输出英雄信息
    print('name = {}, attribute = {}, skill = {}'.format(name,attribute,skill))

# 传入不定长参数
# out_info_hero('李白', '刺客', '突进', '控制','无法选中')
out_info_hero('李白',attribute='刺客',skill='突进')


suml = lambda a, b : a + b
print(suml(2,3))