# chardet:检测编码

import chardet

# 使用chardet
c = chardet.detect(b'Hello, world!')
# 表示这个是ascii编码  'confidence': 1.0  表示检测出的概率是1.0(即100%)
print(c)  # 输出:{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

# 检测GBK编码的中文
data = '离离原上草,一岁一枯荣'.encode('gbk')
print(type(data))
# 检测出的编码是GB2312(注:GBK是GB2312的超集,两者是同一种编码)
print(chardet.detect(data))  # 输出:{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

# 检测UTF-8编码
data = '离离原上草,一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))  # 输出:{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

# 检测日文
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))  # 输出:{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

# -------------------------------
# 示例:
s = b'-ERR \xc4\xfa\xc3\xbb\xd3\xd0\xc8\xa8\xcf\xde\xca\xb9\xd3\xc3pop3\xb9\xa6\xc4\xdc'
# 检测出编码类型b
c = chardet.detect(s)
print('检测:', c)
# 根据编码类型解码
print(s.decode(c.get('encoding')))
