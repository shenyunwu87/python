import sys
print("<==============sys.path=================>")
for path in sys.path:#生成系统路径
    print(path)
print("<==============sys.version=================>")
print(sys.version)#生成版本
print("<==============sys.args=================>")
for argv in sys.argv: #启动项（启动模块明，各种项）
    print(argv)


import time
print("<==============time.time()=================>")
print(time.time())#以距离特定时间点秒的形式输出时间

print("<==============time.ctime()=================>")
stringTime=time.ctime(time.time())
print(stringTime)#以string的形式输出时间

print("<==============time.localtime()=================>")
tLocal=time.localtime(time.time())#以tuple的形式返回time
print(tLocal.tm_year)
print(tLocal.tm_mon)
print("<==============time.localtime()=================>")
print(time.mktime(tLocal))

print("<==============time.strftime()=================>")
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import random
print('<==============random.random()=================>')
print(random.random())#0-1之间的随机小数

print('<==============random.random()=================>')
print(random.randrange(1,10,2))#1-到10 之间步长为2的整数

print('<==============random.choice()=================>')
option=('选项1','option2','option3')
print(random.choice(option))#随机选择一个输出

print('<==============random.shuffle()=================>')
cards=['option1','option2','option3']
random.shuffle(cards)#打乱数字
for iteams in cards:
    print(iteams)

import hashlib
print('<==============hashlib用来加密=================>')
message="我不告诉你"
cryptal=hashlib.md5(message.encode("UTF-8"))
print(cryptal.hexdigest())