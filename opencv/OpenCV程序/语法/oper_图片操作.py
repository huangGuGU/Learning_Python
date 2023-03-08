import numpy as np
import cv2 as cv


# img = np.zeros((3,3),dtype = np.uint8)
# img = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
# print(img)


'''从png保存到jpg'''
# img = cv.imread('cat.png')
# cv.imwrite('cat.jpg',img)



'''生成随机颜色和黑白的照片'''

'''1'''
# # Make an array of 120, 000 random bytes
# random_byte_array = bytearray(os.urandom(120000))
# flat_numpy_array = np.array(random_byte_array)
# # Convert the array to make a 400x300 grayscale image
# grayImage = flat_numpy_array.reshape(300, 400)
# cv.imwrite('random_byte_array.png', grayImage)
# # Convert the array to make a 400x100 color image
# bgr_image = flat_numpy_array.reshape(100, 400, 3)
# cv.imwrite('random_color.png', bgr_image)

'''2'''
# grayImage = np.random.randint(0,256,120000).reshape(300, 400)
# cv.imwrite('random_byte_array.png', grayImage)
#
# bgr_image = np.random.randint(0,256,120000).reshape(200, 200, 3)
# cv.imwrite('random_color.png', bgr_image)


'''看到一个白色的线'''
# img = cv.imread('/Users/hzh/OpenCV程序/photos/black.JPG')
# for i in range(100):
#     img[i,i] = [255,255,255]
#
# cv.imshow('input image',img)
#
# cv.waitKey(0)
# cv.destroyAllWindows()


# img = cv.imread('/Users/hzh/OpenCV程序/photos/black.JPG')
# print(img.item(150,120,0))
# for i in range(120):
#     img.itemset((100,i,0),255)
#
# print(img.item(150,120,0))
# cv.imshow('input image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()


'''使用itemset使（150，120，0）的像素变成了255'''
# img = cv.imread('/Users/hzh/OpenCV程序/photos/black.JPG')
# print(img.item(150,120,0))
# img.itemset((150,120,0),255)
# print(img.item(150,120,0))


# cv.imshow('input image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()




'''让图片没绿色'''
# img = cv.imread('/Users/hzh/OpenCV程序/photos/rainbow.png')
# img[:,:,1] = 0   #遍历所有的像素
# cv.imshow('input image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()


'''图片数据'''
# img = cv.imread('/Users/hzh/OpenCV程序/photos/rainbow.png')
# print(img.shape)  #高宽和通道数
# print(img.size)   #像素大小
# print(img.dtype)  #数据类型


# img = cv.imread('/Users/hzh/OpenCV程序/photos/rainbow.png')
# img[:,:,1] = 0   #遍历所有的像素
# cv.imshow('input image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()


'''捕获摄像头的帧,并保存在本地'''
# cameraCapture = cv.VideoCapture(0)
# fps = 30
# size = (int(cameraCapture.get(cv.CAP_PROP_FRAME_WIDTH)),int(cameraCapture.get(cv.CAP_PROP_FRAME_HEIGHT)))
# videoWriter = cv.VideoWriter('my output vid.avi',cv.VideoWriter_fourcc('I','4','2','0'),fps,size)
#
# success , frame = cameraCapture.read()
# numFramesRemaining = 10*fps-1
# while success and numFramesRemaining>0:
#     videoWriter.write(frame)
#     success, frame = cameraCapture.read()
#     numFramesRemaining -=1
# cameraCapture.release()

