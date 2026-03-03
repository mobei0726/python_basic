# 使用比较运算符比较数据，相同是True,不相同是Flase
# 数据类型要保持一致

# 判断是否相等用==
a = 5
b = 5
print(a == b)

# 判断是否不相等用!=
c= 5
d = 6
print(c != d)

# 判断大于用>
e = 5
f = 6
print(e > f)

# 判断小于用<
g = 5
h = 6
print(g < h)

# 判断大于等于用>=
i = 7
j = 6
print(i >= j)

# 判断小于等于用<=
k = 5
l = 6
print(k <= l)

# 以上比较运算符对于字符串也适用
m = 'abc'
n = 'abc'
print(m == n)

# 判断大小用unicode编码来判断
# 查看unicode编码用ord()，但里面的内容用单个字符
o = '我'
p = '中国'
# ord('我')
print(ord('我'))
print(o > p)