text = input('请输入加密的文字：')
secret = ''
for t in text:
    secret += chr((ord(t) + 1))
print(f'加密后为：{secret}')
