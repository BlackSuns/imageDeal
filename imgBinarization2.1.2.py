# 图像二值化
# Python 3.7
# Author:Xujintao
# Github:
#Borrowed from https://www.jb51.net/article/198147.htm

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2 as cv


def imgBinarization(image):
    # 把输入图像灰度化
    grayImg = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # image to list
    img = np.array(image)
    print(img)
    plt.title('hist figure')
    # 数据,a.flatten()把a降到一维
    arr = img.flatten()
    print(arr)
    n, bins, patches = plt.hist(arr, bins=256, density=0, facecolor='green')
    # n: 直方图向量，是否归一化由参数normed设定，bins: 返回各个bin的区间范围，patches: 返回每个bin里面包含的数据，是一个list
    plt.show()
    mean = arr.sum() / len(arr)
    print("mean:", mean)
    # ret: Image threshold
    # binary: Threshold processing image outcome
    ret, binary = cv.threshold(grayImg, mean, 255, cv.THRESH_BINARY)
    return binary


src = cv.imread('myImg.jpg')
cv.namedWindow('input_image', cv.WINDOW_NORMAL)  # 设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
imgBinarization(src)
cv.namedWindow("binary2", cv.WINDOW_NORMAL)
binarizationImg = cv.imshow("binary2",imgBinarization(src) )
binarizationImg.save("binarizationImg.jpeg")
cv.waitKey(0)#cvWaitKey()函数的功能是不断刷新图像，频率时间为delay，单位为ms。
cv.destroyAllWindows()
