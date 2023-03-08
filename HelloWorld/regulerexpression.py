import re
print('<==============match()=================>')
msg="古力娜扎迪丽热巴佟丽娅"
pattern=re.compile("佟丽娅")
print(pattern.match(msg))
msg="佟丽娅古力娜扎迪丽热巴"
print(pattern.match(msg))
print(re.match("佟丽娅","佟丽娅古力娜扎迪丽热巴"))
print('<==============search()=================>')
print(re.search("佟丽娅","佟丽娅古力娜扎迪丽热巴").group())