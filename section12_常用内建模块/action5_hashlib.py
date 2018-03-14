# hashlib
# hashlib提供了常见的摘要算法,如MD5、SHA1等
# 摘要算法:又称为哈希算法、散列算法.它通过一个函数
# ,把任意长度的数据转换成一个长度固定的数据串(通常是16进制的字符串表示)

import hashlib

# 示例:计算一个字符串的MD5值
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # 输出:d26a53750bc40b38b65a520292f69306

# 分块计算:
md5 = hashlib.md5()
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))
# 结果不变
print(md5.hexdigest())  # 输出:d26a53750bc40b38b65a520292f69306
# 注:MD5是最常见的摘要算法 生成结果是固定的128 bit字节,通常用一个32位的16进制字符串表示


# SHA1的调用和MD5的调用方式一样
sha1 = hashlib.sha1()
sha1.update('how to use md5 '.encode('utf-8'))
sha1.update('in python hashlib?'.encode('utf-8'))
print(sha1) # 输出:<sha1 HASH object @ 0x10294a878>
# 注:SHA1的结果是160bit字节,通常用一个40位的16进制字符串表示
