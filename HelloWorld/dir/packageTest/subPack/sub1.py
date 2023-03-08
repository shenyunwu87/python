import packageTest
print("<=============sub1被执行被执行============》")

def sub1fun():
    print("<=============sub1fun被调用============》")

class Sub1Class():
    print("<=============Sub1Class 主函数被 被调用============》")
    def __int__(self):
        print("<=============Sub1Class init 被调用============》")