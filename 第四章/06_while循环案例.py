print('您现在身处密室中，只有正确回答问题您才能脱困/1+1=？')
question = '你是什么人？'
answer = '神'
guess = ''

while guess != answer:
    print(f'请回答问题：{question}')
    guess = input('请输入答案:')
    if guess == answer:
        print('回答正确！')
    else:
        print('回答错误！')
