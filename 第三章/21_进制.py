# 使用0b表示二进制
# print(0b100)
# # 使用0o表示八进制
# print(0o1034)
# # 使用0x表示十六进制
# print(0x1cf)
# 注意:0b,0o,0x,只是程序员看的,输出后还是十进制

# 使用bin()将十进制转换为2进制
# print(bin(4))
# # 使用oct()将十进制转换为8进制
# print(oct(540))
# # 使用hex()将十进制转换为16进制
# print(hex(463))

# 使用int将指定进制的字符串形式转换为十进制
print(int('0b100',2))
print(int('0o1034',8))
print(int('0x1cf',16))