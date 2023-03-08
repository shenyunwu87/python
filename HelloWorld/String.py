# 字符串运算
ord("沈")  # 转换成Unicode
chr(3613)  # 数字转换成字符
text = '''name="沈援武“ 
age="36"'''  # 三引号可以多行
print(text)
print(len(text))  # 查长度
print("hello" * 3)  # 可以重复
print("不换行", end="")  # 不换行
print("没换行")
print(text[2])  # 取第三个字符
print(text[0:3])  # 取第1到4前字符（包头部包尾）
print(text[0:4:2])  # 隔2取第1到4前字符（包头部包尾）
print(text[-5:])  # 取倒数5个字符（包头部包尾）
text = "to be or NOT to be aa"
splitedText = text.split("be")  # 按be分割
print("be".join(splitedText))  # 用be连接
splitedText.append("aa")
print(splitedText)  # 后加元素
print("be" in text)  # 判断包含字符串与否
print(text.startswith("to"))  # 开头的是否为to
print(text.endswith("aa"))  # 尾部是否为aa
print(text.find("be"))  # to 第一次出现位置
print(text.rfind("be"))  # 最后一次出现位置
print(text.count("to")) #to 出现多少次
print(text.isalnum())#是否为数字
print(text.strip())#去除首尾空格
print(text.strip('t'))#去除首尾t
print(text.lstrip('t'))#去除首t
print(text.rstrip('a'))#去除尾所有a
print(text.capitalize())#首字母大写
print(text.title())#每个单词首字母大写
print(text.upper())#所有字母都大写
print(text.lower())#所有字母都小写
print(text.swapcase())#所有字母大小写反转
print(text.center(30, '*' ))#*排版居中
print(text.ljust(30, '*' ))#*排版靠左
print(text.rjust(30, '*' ))#*排版靠右
print("hello".isalpha())#是否字母组成（含汉子）
print("12.35".isdigit())#是否纯数字
print("TT".isupper())#是否大写
print("tt".islower())#是否小写
print("\n\t ".isspace())#是否空白
#可变字符串
import io
sio=io.StringIO(text)
print(sio.getvalue())
sio.seek(3) #光标移动到第4个字母
sio.write("B")
print(sio.getvalue())