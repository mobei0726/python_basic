# 浮点型就是带小数点的数字，小数点后面是0也算
height = 180.2
price = 120.0
print(type(price))

# 浮点型（大数字）的科学计数法，e表示10，后面几次方就跟几，例如下面
speed_sound =3.4e2
speed_sound1 =3.4e+2
speed_sound2 =3.4E2
speed_sound3 =3.4e2
print(speed_sound,speed_sound1,speed_sound2,speed_sound3)

# 浮点型（小数字）的科学计数法，e表示10，后面几次方就跟（负的）几，例如下面
one_ml=1e-3
one_ml1=1E-3
print(one_ml,one_ml1)