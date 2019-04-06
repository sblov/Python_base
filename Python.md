# Python

## 数据类型

### 数值

​	**int	、 float**

​	Python中的整数的大小没有限制，可以使一个无限大的整数

​	`a = 99999999999999999999999999999999999999999**100`

​	如果数字的长度过大，可以使用下划线作为分隔符

​	`a = 123_334_5343`

​	十进制不能以0开头、二进制：0b、八进制：0o、十六进制：0x；数值打印一定是以十进制的形式显示

​	浮点数（小数），在Python中所有的小数都是float类型

### 字符串

​	**str**

​	使用三重引号表示的字符串，可以换行，会保留字符串中的格式

​	CodeCharts  所有unicode字符

​	字符串不能和其他的类型进行加法运算 

​	在创建字符串时，可以在字符串中指定占位符

​	%s 在字符串中表示任意字符串

​	%f 浮点数占位符

​	%d 整数占位符

​	可以通过在字符串前加一个f来创建一个格式化字符串；格式化字符串中可以直接嵌入变量

​	字符串复制（将字符串与 数字相乘）

```python
a = 123
# 多个参数
print('a=',a)

# b = 'hello %3.5s'%'asdfgh' # 字符串长度在3-5之间
# b = 'hello %s'%1234
# b = 'hello %.2f'%11.2324	# 保留小数点后两位
b = 'hello %d'%123.76789
print(b)
# 占位符
print('a = %s'%a)

c = f'hello {a} {b}'
# 格式化字符串
print(f'c = {c}')
# 字符串复制
print(b * 3)
```

### 布尔与空

​	**bool**

​	布尔值实际上属于整型，True为1，False为0

​	**NoneType**

​	None（空值），专门表示不存在

### 类型检查

​	type()，返回类型结果

### 对象结构

**ID（标识）**

​	通过id（）函数查看对象id

​	id由解析器生成，在cpython中，id就是对象的内存地址

​	对象一旦创建，id永远不能变

**type（类型）**

​	标识对象当前所属类型

​	type（）查看类型

​	Python为强类型语音，一旦创建类型不能修改

**value（值）**

​	对象中存储具体数据

​	不可变对象与可变对象（值是否可变）

### 类型转换

​	**int()**

​	浮点数取整

​	合法整数字符串，否则报ValueError

​	不可转换为整数的对象，直接ValueError

​	**float()**

​	**str()**	

​	**bool()**

​	任何对象可为布尔值

​	表示空的对象转换为False，其余为True（0，None，''，......）

### 运算符

​	// 	整除，只保留计算后的整数

​	is/is not	    比较两个对象是否为同一对象（比较id）	

​	not		对于非布尔值，先转换为布尔，再取反

​	and	/or		短路运算，and优先级高于or

## 高阶函数

​	将函数作为参数或返回值的函数

### 匿名函数

```python
lis = [1,2,3,4]

l = list(map(lambda i : i+1,lis))

print(l)
========================================================
l = [45,5,7,'3','7','9',22]

# 不会改变list的值，而是返回新的list，将int()方法传给key，作为比较值的函数
print(sorted(l,key = int))

l.sort(key=int)
print(l)

```

### 闭包

```python
# 闭包：函数嵌套，将函数作为返回值返回

def make_ave():
	pass
	nums = []

	def ave(n):
		pass
		nums.append(n)
		return sum(nums)/len(nums)
	return ave

ave = make_ave();

print(ave(10))
print(ave(20))


```

### 装饰器

```python
def begin_end(fn):
	# 用来对其他函数进行扩展
	# *args：接收所有单个参数为元组，**kwargs：接收所有键值参数为字典
	def new_function(*args,**kwargs):
		print("begin---")
		fn(*args,**kwargs)
		print("end---")

	#将传入的方法增强后返回
	return new_function;


@begin_end
def test(str):
	pass
	print(str)

# 当前调用的方法实质为返回的增强方法
test("test")
```

## 类

### 对象创建

```python
class test(object):
	"""docstring for test"""
	name = 'default'
    # self为默认传递的实例对象本身，方法中不能直接访问方法类中的属性
	def __init__(self, arg):
		super(test, self).__init__()
		self.arg = arg
		print(self.name)
		
t = test("test")

# 检查t对象是否为test的实例
print(isinstance(t,test))

t.name = 'lov'
print(t.name)

# <class 'type'>
# 所有对象都是type的实例，类也是对象
print(type(test))

# 创建test类，对应内存中一块区域，类型为type
# 创建test类实例时，有开辟新的内存空间创建test类型的对象
# 在变量-id的映射表中，将id赋给变量 
```

## 文件

```python
text = 'this a test file'
# 读写方式打开文件，没有即创建，相对当前文件路径
my_file = open('my_file.txt','r')

# my_file.write(text)
result = my_file.read()
print(result)

my_file.close()
```

## 复制

`copy.copy()` : 复制当前对象引用的内容到一个新的对象，引用的内容属于新的对象，但是内容如果还要对其他对象的引用，也会保留复制

`copy.deepcopy()` : 深度复制，将指向的内容，包括引用的内容，完全复制到新的对象

```python
import copy
a = [1,2,4,[5,6,7]]

# 仅复制当前对象内容
b = copy.copy(a)

print(id(a) == id(b)) # False
print(id(a[3]) == id(b[3])) # True 

# 复制所有相关内容
b = copy.deepcopy(a)

print(id(a) == id(b)) # False
print(id(a[3]) == id(b[3])) # False
```

## 正则

### match&search

```python
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
```

### 检索替换

```python
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
```

### compile

​	compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。 

```python
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
```

### findall

​	在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。 

```python
# findall(string[, pos[, endpos]])
# string 待匹配的字符串。
# pos 可选参数，指定字符串的起始位置，默认为 0。
# endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
```

### re.finditer

​	和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。 

```python
# re.finditer(pattern, string, flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() )
```

### re.split

```python
# re.split(pattern, string[, maxsplit=0, flags=0])
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等

print(re.split('\W+', 'runoob, runoob, runoob.'))

print(re.split('(\W+)', ' runoob, runoob, runoob.') )

print(re.split('\W+', ' runoob, runoob, runoob.', 1) )

print(re.split('a*', 'hello world')) 
```

## Mysql

```python
import pymysql
# 连接数据库
db = pymysql.connect(host='127.0.0.1',
	port=3306,
	user='root',
	password='997103',
	database='lov',
	charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询  
cursor.execute("select version()")
# 使用 fetchone() 方法获取单条数据
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
data = cursor.fetchone()

print(data)

#创建数据库--------------------------------
# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
 
# cursor.execute(sql)

# insert语句--------------------------------
# SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
	# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       # LAST_NAME, AGE, SEX, INCOME) \
       # VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       # ('Mac', 'Mohan', 20, 'M', 2000)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()

# 查询select--------------------------------
# SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#        # 打印结果
#       print ("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
#              (fname, lname, age, sex, income ))
# except:
#    print ("Error: unable to fetch data")

# update 更新数据--------------------------------
# SQL 更新语句
# sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()


# delete删除--------------------------------
# SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()


# 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。

# commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。

db.close()
```

## 多线程

## tkinter

## pip

### 手动安装

1、`https://pypi.python.org/pypi/pip#downloads` 下载pip包

2、解压执行 `Python setup.py install  `

3、设置环境（看情况），`where pip` 查看pip命令文件

### 命令

`python -m pip install --upgrade pip`  ：更新pip

`pip list` ：列出安装的模块

`pip install 模块名` ：安装模块

`pip show 模块名` ：查看安装模块的信息

`pip install -U  模块名` ：升级指定模块

# Django