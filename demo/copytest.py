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

