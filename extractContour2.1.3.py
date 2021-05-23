from PIL import Image
from PIL import ImageFilter

myimg = Image.open("myImg.jpg")
region = (1240, 0, 3650, 1850)
myface = myimg.crop(region)
print('截取图像区域的尺寸' + str(myface.size))
def darker(x):
    return x * 2.5
myface = myface.resize((1000, 1000))
#像素加深
myface = Image.eval(myface, darker)


myface = myface.filter(ImageFilter.EDGE_ENHANCE_MORE)
#提取轮廓
myface = myface.filter(ImageFilter.CONTOUR)
#(𝑥,𝑦)=(160,200)
myimg.paste(myface, (3000,1000,3000+myface.width,1000+myface.height))
myimg.save("Contour.png")
myimg.show()