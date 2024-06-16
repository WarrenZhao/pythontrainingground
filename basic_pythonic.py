# python中的倒序遍历实现
# 1. 使用reversed()函数

items = ["a", "b", "c"]
for item in reversed(items):
    print(item)

# 2.利用下标使用range函数
for i in range(len(items)-1, -1, -1):
    print(items[i])

# 3.利用切片实现
print(items[::-1])