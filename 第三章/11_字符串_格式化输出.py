name = '张三'
gender = '男'
weight = 81.25
age = 18

#第一种写法：使用加号连接,但是只能连接字符串
info1='我叫'+name+'，我是'+gender+'生'
print(info1)

#第二种写法：使用占位符%
info2='我叫%s,我的性别是%s,我的体重是%f,我的年龄是%i' %(name,gender,weight,age)
print(info2)

#第三种写法：使用f_string，最优的方式
info3=f'我叫{name},我是{gender}生，我的体重是{weight}，我的年龄是{age}'
print(info3)