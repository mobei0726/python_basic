print('马拉松比赛报名审核')

age = int(input('请输入你的年龄：'))
has_report = input('请输入是否提交体检报告（是/否）：')
level = int(input('请输入会员等级（1/2/3）：'))

if 18 <= age <= 45:
    print('您的参赛年龄负荷标准')
    if has_report=='是':
        print('您的体检报告提交状态符合要求，您可以参加比赛')
        if level==1:
            print(f'报名通过，由于您是{level}级会员，比赛结束后您的礼物是纪念T恤')
        elif level==2:
            print(f'报名通过，由于您是{level}级会员，比赛结束后您的礼物是专业跑鞋')
        elif level==3:
            print(f'报名通过，由于您是{level}s级会员，比赛结束后您的礼物是运动耳机')
        else:
            print('您的会员等级不符合要求')
    else:
        print('审核不通过')
else:
    print('审核不通过')
