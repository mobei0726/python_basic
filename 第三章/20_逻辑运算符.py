# and判断两边值是否都为True
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# and通过程序执行来判断
print(3 > 2 and 3 > 2)
print(3 > 2 and 2 > 7)
print(2 > 7 and 3 > 2)
print(2 > 7 and 2 > 7)

# and具备逻辑短路的能力
print(False and 3 / 0)
print(True and 3 / 0)

# and返回的不一定是布尔类型，也可能是参与运算的值得本身
# and会先看左边，如果左边为假，则直接返回左边，否则返回右边
# 若参与运算的值不是布尔类型，则先转换为布尔类型在进行运算
print(False and True)
print(1 - 1 and True)
print(True and 2 - 2)
print(True and 4 + 1)

# or：只要两边有一个为True，就返回True
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# 通过程序运算判断
print(3 > 1 or 3 > 1)
print(3 > 1 or 7 < 2)
print(7 < 2 or 3 > 1)
print(7 < 2 or 7 < 2)

# or也具备逻辑短路的能力
print(True or 3 / 0)
print(False or 3 / 0)

# or返回的不一定是布尔类型，也可能是参与运算的值得本身
# or会先看左边，如果左边为真，则直接返回左边，否则返回右边
# 若参与运算的值不是布尔类型，则先转换为布尔类型在进行运算
print(False or True)
print(1 - 1 or True)
print(True or 2 - 2)
print(3+4 or 4 + 1)

# not是取反操作，并且只能返回布尔值
# 若参与运算的值不是布尔类型，则先转换为布尔类型在进行运算
print(not True)
print(not False)
print(not 1+1)
print(not 1-1)
print(not '你好')
print(not '')