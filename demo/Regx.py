import re

# re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www','www.google.com').span())

print(re.match('com','www.google.com'))

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")


# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('com','www.google.com'))

####################################################################

# re.sub(pattern, repl, string, count=0)
# pattern : 正则中的模式字符串。
# repl : 替换的字符串，也可为一个函数。
# string : 要被查找替换的原始字符串。
# count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

phone = "2004-959-559 # 这是一个电话号码"
 
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : ", num)
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)

# repl 为函数
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

###################################################################
# re.compile(pattern[, flags])
# pattern : 一个字符串形式的正则表达式
# flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# 	re.I 忽略大小写
# 	re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# 	re.M 多行模式
# 	re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
# 	re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# 	re.X 为了增加可读性，忽略空格和' # '后面的注释

pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m) 

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)                                         # 返回一个 Match 对象

print(m.group(0))   # 可省略 0

print(m.start(0))   # 可省略 0

print(m.end(0))     # 可省略 0

print(m.span(0))    # 可省略 0

############################################################
# findall(string[, pos[, endpos]])
# string 待匹配的字符串。
# pos 可选参数，指定字符串的起始位置，默认为 0。
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)

############################################################
# re.finditer(pattern, string, flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )

# re.split(pattern, string[, maxsplit=0, flags=0])
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

print(re.split('\W+', 'runoob, runoob, runoob.'))

print(re.split('(\W+)', ' runoob, runoob, runoob.') )

print(re.split('\W+', ' runoob, runoob, runoob.', 1) )

print(re.split('a*', 'hello world')) 
