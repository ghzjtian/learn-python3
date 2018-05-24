#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开


#来看看最常见的图像缩放操作，只需三四行代码：

from PIL import Image

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('/Users/tianzeng/Desktop/ScreenShot2018-05-23_16.27.11.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/tianzeng/Desktop/thumbnail.jpg', 'jpeg')


