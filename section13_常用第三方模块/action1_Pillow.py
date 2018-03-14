# Pillow:图像处理标准库 在PIL基础上创建的兼容版

# 操作图像
from PIL import Image, ImageFilter

# 示例:
# 常见的图像缩放操作

# 1.打开一个图片
image = Image.open('test.jpg')
# 2.获取图片尺寸
w, h = image.size
print('图片宽:', w, '图片高:', h)  # 输出:图片宽: 750 图片高: 1334
# 3.缩放到50%  // :表示返回商的整数部分  取整除
image.thumbnail((w // 2, h // 2))
print('图片缩放宽:', w // 2, '图片缩放高:', h // 2)  # 输出:图片缩放宽: 375 图片缩放高: 667
# 4.把缩放后的图片用jpeg格式保存
image.save('thumbnail.jpg', 'jpeg')

# 设置图片的模糊效果
# 1.打开图片
im = Image.open('test.jpg')
# 2.应用模糊滤镜
im1 = im.filter(ImageFilter.BLUR)
im1.save('filter.jpg', 'jpeg')

# ---------------------------------
# PIL的ImageDraw提供了一系列绘图方法

# 示例:生成字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 生成随机字母
def randomChar():
    return chr(random.randint(65, 90))


# 生成随机颜色
def randomColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 生成随机颜色2
def randomColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 设置图片宽高:240*60
width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randomColor())
        pass
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomColor2())

# 模糊
image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

# 显示预览效果
# image.show()
