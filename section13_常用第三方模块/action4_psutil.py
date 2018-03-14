# psutil:获取系统信息

import psutil

# 获取cpu信息

# 返回cpu逻辑数量
print(psutil.cpu_count())
# 返回cpu物理核心  返回2表示:双核超线程  返回4表示:4核非超线程
print(psutil.cpu_count(logical=False))

# 统计CPU的用户/系统/空闲时间
print(psutil.cpu_times())  # 输出:scputimes(user=114290.89, nice=0.0, system=63190.83, idle=923958.39)

# 实现类似top命令(注:top命令 类似于windows的任务管理器 实时显示资源占用情况) 每秒刷新一次 刷新10次
for x in range(1):
    # 返回一个list
    print(psutil.cpu_percent(interval=1, percpu=True))


# -------------------------------------
# 获取内存信息
# 1.获取物理内存信息 返回的是以字节为单位的整数
print(psutil.virtual_memory())
# 输出:svmem(total=8589934592, available=2316099584, percent=73.0, used=6840037376
# , free=147599360, active=2323935232, inactive=2168500224, wired=2347601920)

# 2.获取交换内存信息 返回的是以字节为单位的整数
print(psutil.swap_memory())
# 输出:sswap(total=3221225472, used=2101608448, free=1119617024, percent=65.2, sin=51983056896, sout=2057584640)


# -------------------------------------
# 获取磁盘信息
# 1.获取磁盘分区信息
print(psutil.disk_partitions())
# 2.获取磁盘使用情况
print(psutil.disk_usage('/'))
# 3.磁盘I/O
print(psutil.disk_io_counters())


# -------------------------------------
# 获取网络信息
# 1.获取网络接口和网络连接信息
# 1.1 获取网络读写字节/包的个数
print(psutil.net_io_counters())
# 1.2 获取网络接口信息
print(psutil.net_if_addrs())
# 1.3 获取网络接口状态
print(psutil.net_if_stats())
# 1.4 获取网络连接信息(注:这里会报AccessDenied 原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限,这种情况下，可以退出Python交互环境，用sudo重新启动)
# print(psutil.net_connections())


# -------------------------------------
# 获取进程信息
# 1.1 获取所有进程ID
print(psutil.pids())
# 1.2 获取指定进程ID获取进程信息
p = psutil.Process(37009)
# 进程名
print(p.name())
# 进程路径
print(p.exe())
# 工作目录
print(p.cwd())
# 启动命令行
print(p.cmdline())
# 父进程ID
print(p.ppid())
# 父进程
print(p.parent())
# 子进程列表
print(p.children())
# 进程状态
print(p.status())
# 进程用户名
print(p.username())
# 进程创建时间
print(p.create_time())
# 进程终端
print(p.terminal())
# 进程使用的cpu时间
print(p.cpu_times())
# 进程使用的内存
print(p.memory_info())
# 进程打开的文件
print(p.open_files())
# 进程相关网络连接
print(p.connections())
# 进程的线程数量
print(p.num_threads())
# 所有线程信息
# print(p.threads())
# 进程环境变量
print(p.environ())
# 结束进程
# print(p.terminate())

# psutil还提供了一个test()函数，可以模拟出ps命令的效果




