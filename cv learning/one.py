import cv2

""" 一、cv的基本操作：读取显示图片、灰度、模糊处理
# imread读取图片 控制显示 退出
img = cv2.imread('logo.png')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 转换为灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 模糊处理
blurred_img = cv2.GaussianBlur(img, (21, 21), 0)
cv2.imshow('blurred image', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows() """

# 二、边缘检测与更多图像处理

