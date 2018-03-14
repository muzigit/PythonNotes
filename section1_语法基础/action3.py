#  条件判断
age = 18

# if...elif...else的定义
if age < 18:
    print('未成年')
elif age == 18:
    print('刚好成年')
else:
    print('已成年')

# 练习:
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.78  # 单位:m
weight = 60  # 单位:kg

# ** 表示求平方
BMI = weight / (height ** 2)

# round():对浮点数进行四舍五入  参数二表示需要保留多少位小数点
BMI = round(BMI, 2)


def switchBmi(dec):
    print('您的BMI值是', BMI, dec)


if BMI < 18.5:
    switchBmi(dec='过轻')
elif BMI > 18.5 and BMI < 25:
    switchBmi(dec='正常')
elif BMI > 25 and BMI < 28:
    switchBmi(dec='过重')
elif BMI > 28 and BMI < 32:
    switchBmi(dec='肥胖')
else:
    switchBmi(dec='严重肥胖')
