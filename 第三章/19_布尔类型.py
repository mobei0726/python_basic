# 使用定义来识别布尔类型（boolean,简写为bool）,True和False的首字母都是大写
# a=True
# b=False
# print(type(a),a)
# print(type(b),b)

# 通过程序执行来判断布尔类型
# a = 7 > 5
# b = 5 >= 6
# print(type(a), a)
# print(type(b), b)

# 布尔类型是int类型的子类型，True表示1，False表示0
# print(True + 1)
# print(False + 1)

# 使用bool()将数字可以转换为布尔类型,除0以外的所有数字转换为布尔类型都为True
# print(bool(1))
# print(bool(2.3))
# print(bool(-8))
# print(bool(1.8e3))
# print(bool(0))
# print(bool(8 - 8))

# python中任何非空字符串转为布尔值都为True
print(bool('你好'))
print(bool('2.2'))
print(bool('5'))
print(bool(''))
