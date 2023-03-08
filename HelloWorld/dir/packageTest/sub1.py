print("<=============sub1被执行被执行============》")

def sub1fun():
    print("<=============sub1fun被调用============》")

class Sub1Class():
    print("<=============Sub1Class 主函数被 被调用============》")
    def __int__(self,num):
        print("<=============Sub1Class init 被调用============》")

    def __new__(cls, *args, **kwargs):
        super().__new__(cls)
        print("<=============Sub1Class new 被调用============》")

    def __call__(self, *args, **kwargs):
        print("<=============Sub1Class call 被调用============》")