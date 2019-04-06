text = 'this a test file'
# 读写方式打开文件，没有即创建，相对当前文件路径
my_file = open('my_file.txt','r')

# my_file.write(text)
result = my_file.read()
print(result)

my_file.close()