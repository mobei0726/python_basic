# 前序知识
# print('北京', end=' ')
# print('欢迎您', end='!')

# 使用for循环打印九九乘法表
for row in range(1, 10):
    for item in range(1, row + 1):
        print(f'{item}*{row}={row * item}', end='\t')
    print()# 每行结束后换行

# 使用while循环打印九九乘法表
row = 1
while row <= 9:
    item = 1
    while item <= row:#项数循环只到row
        print(f'{item}*{row}={row * item}', end='\t')
        item += 1
    row += 1
    print()# 每行结束后换行
