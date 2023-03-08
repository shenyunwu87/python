
#字符串格式化
text="name:{0},age:{1}"
print(text.format("shen", 36))
stringText="name:{name},age:{age}"
print(stringText.format(name="shen",age=18))

text="name:{0:*^8},age:{1}"#用*号填充8格中对齐
text="name:{0:*>8},age:{1}"#用*号填充8格右对齐
text="name:{0:*<8},age:{1}"#用*号填充8格左对齐
print(text.format("shen", 36))