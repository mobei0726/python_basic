# continue:跳过本次循环执行下一次循环
# break：直接终止后续循环
for day in range(1,4):
    print(f'第{day}天健身计划已完成')
    if day==2:
        continue
    print(f'第{day}天已完成')

for day in range(1,4):
    print(f'第{day}天健身计划已完成')
    if day ==2:
        break
    print(f'第{day}天已完成')