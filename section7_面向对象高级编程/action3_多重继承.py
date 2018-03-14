# 多重继承
# MixIn(混入)的概念: 通常情况下,一个类都是单一继承下来的 如果一个类需要'混入'额外的功能,通过多重继承即可实现
# 例如:Ostrich 除了继承Bird 还继承Runnable,这种设计称之为MixIn
# 目的:MixIn的目的就是给一个类增加多个功能

# 示例:
# Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型
# ，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

from socketserver import *


# 编写一个多进程的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass


# 编写一个多进程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


