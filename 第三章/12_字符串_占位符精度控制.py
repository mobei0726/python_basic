name = '张三'
gender = '男'
weight = 81.25
age = 18

# 精度控制%m.n控制，m控制位数，n控制精度，正/负控制靠右/左
info2='我叫%s,我的性别是%s,我的体重是%8.3f,我的年龄是%i' %(name,gender,weight,age)
print(info2)