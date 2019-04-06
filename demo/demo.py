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