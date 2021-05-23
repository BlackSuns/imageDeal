 # * RGB分离部分代码*

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

#设置中文显示
plt.rcParams['font.sans-serif']='fangsong'
plt.rcParams['font.size'] = 8

src = Image.open('split.jpg')
img = np.array(Image.open('split.jpg'))
print(img)
plt.subplot(221)
plt.title('orignal')
plt.imshow(img)
plt.subplot(222)
plt.title('R-缩放')
reduceimg = src.resize((50,50))
reduceimg = np.array(reduceimg)
#img[:, :, 0]，其中0表示红色是RGB分量通道0
plt.imshow(reduceimg[:, :, 0], cmap='gray')
plt.title('G-镜像+旋转')
rotImg = src.rotate(180)
rotImg = src.rotate(90)
plt.subplot(223)
rotImg = np.array(rotImg)
plt.imshow(rotImg[:, :, 1], cmap='gray')#图像矩阵第
plt.subplot(224)
plt.imshow(img[:, :, 2], cmap='gray')
#完成其余部分#

plt.show()
