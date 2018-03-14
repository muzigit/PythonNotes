# datetime
# datetime是python处理日期和时间的标准库

from datetime import datetime

# 获取当前日期和时间
d = datetime.now()
print(d)  # 输出:2018-03-07 11:03:05.541638
print(type(d))  # 输出:<class 'datetime.datetime'>

# 获取指定时间和日期
dt = datetime(2018, 3, 7, 11, 7, 40)  # 注:年月日参数必须要传否则会报错  之后构建一个datetime对象
print(dt)  # 输出:2018-03-07 11:07:40

# ----------------------------------
# datetime 转换为 timestamp(时间戳)
# 新纪元时间(epoch time):1970年1月1日 00:00:00 UTC+00:00时区的时刻 记为0
# 1970年以前的时间timestamp,记为负数  当前时间就是相对于epoch timed的秒数
# timestamp 没有时区概念

# timestamp()方法:将一个datetime 转换为 timestamp
ts = dt.timestamp()
# ts 是一个浮点数 如有小数点,小数点表示毫秒
print(ts)  # 输出:1520392060.0

# ----------------------------------
# timestamp(时间戳) 转换成 datetime
# fromtimestamp():将timestamp 转换成 datetime
# datetime 有时区概念

fts = datetime.fromtimestamp(ts)
# 输出的是本地时间
print(fts)  # 输出:2018-03-07 11:07:40

# timestamp可以转换到UTC标准时区(也就是UTC+0:00时区)的时间:
utcts = datetime.utcfromtimestamp(ts)
print(utcts)  # 输出:2018-03-07 03:07:40

# ----------------------------------
# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)  # 输出:2015-06-01 18:19:59

# ----------------------------------
# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))  # 输出:Wed, Mar 07 11:42

# ----------------------------------
# datetime加减
# 对datetime加减需要导入 timedelta这个类  可以直接使用 + 或 - 进行运算
from datetime import timedelta

print(now + timedelta(hours=10))  # 输出:2018-03-07 21:45:53.396678
print(now - timedelta(days=1))  # 输出:2018-03-06 11:59:19.094080
print(now + timedelta(days=2, hours=12))  # 输出:2018-03-09 23:59:58.185975

# ----------------------------------
# 本地时间转换成UTC时间
# 一个datetime 有一个时区属性tzinfo 但是默认是None 因此无法区分datetime是哪个时区的,除非强行给datetime设置一个时区
from datetime import timezone

# 创建时区 UTC+8:00
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8)
print(dt)   # 输出:2018-03-07 13:45:23.965154+08:00

# 以上代码 只有当时区恰好是 UTC+8:00 时,上述代码是正确的 否则 不能强制设置时区为 UTC+8:00


# ----------------------------------
# 时区转换
# 通过utcnow() 获取到当前的utc时间 再转换为任意时区的时间

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)   # 输出:2018-03-07 05:49:46.730254+00:00

# astimezone()

# 转换时区为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)   # 输出:2018-03-07 13:51:32.170256+08:00

# 转换时区为东京时间
dj_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(dj_dt)    # 输出:2018-03-07 14:53:12.413589+09:00

# 将bj_dt转换为东京时间
dj_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(dj_dt)    # 输出:2018-03-07 14:55:31.229091+09:00

# 注:时区转换,并不是一定要从 UTC+0:00时区转换到其他时区,任何带时区的datetime都可以转换

