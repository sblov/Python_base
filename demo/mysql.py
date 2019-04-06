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

#创建数据库
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

# insert语句
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

# 查询select
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

# update 更新数据
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


# delete删除
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