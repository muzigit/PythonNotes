# hmac
# Hmac算法(Keyed-Hashing for Message Authentication) 通过一个标准算法,在计算哈希的过程中,把key混入计算过程中

import hmac

# 使用hmac实现带key的哈希
message = b'Hello,world!'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
# 如果字符串过长  可以多次调用h.update(msg)
print(h.hexdigest())    # 输出:21db988f124ebc9fade5492afb9df52d
# 注:message 和 key都是bytes类型
