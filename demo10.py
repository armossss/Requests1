# re库的Match对象练习
import re
# 1.先获取一个Match对象
string = 'PYANBNCNDN'  #待匹配的文本

mac =re.search(r'PY.*N', string)

# 使用Match对象名.group方法只能够查看第一个匹配的字符串，如果需要查看多个匹配到的结果，
# 我们可以使用re.findall()或者是re.finditer
print(mac.group(0))

# 1.使用re.findall()
print(re.findall(r'PY.*N', string))
# 2.使用re.finditer,这个方法返回的是一个迭代器
matchlist =[i for i in re.finditer(r'h+', string)]
print(matchlist)


print('='*20, "现在学习Match对象.start()方法", '='*20)
# 使用Match对象.start() 返回一个匹配字符串在原始字符串的开始位置
print(mac.start())

print('='*20, "现在学习Match对象.end()方法", '='*20)
# 使用Match对象.end() 返回一个匹配字符串在原始字符串的结束位置
print(mac.end())

print('='*20, "现在学习Match对象.span()方法", '='*20)
# 使用Match对象.span() 返回(Match对象.start(), Match对象.span()方法)
print(mac.span())