a = 2
# 取类地址和类名
print(id(a))
print(type(a))
del a  # 删除a
# 转化
float(3)  # 转化为浮点数
int(3.45)  # 取int值
str(3.24)  # 转化为字符串
a = 3 ** 2  # 3的2次方
round(3.25)  # 四舍五入

import time

print(time.time())

# 逻辑运算
True or False
True and False
not True
a = 4
#print(a is 4)  # 判断是否同一地址
def add(x: int, y: int) -> int:
    return x + y
print(add ("hellow"," world"))