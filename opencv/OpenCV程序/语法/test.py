import cv2 as cv
# def get_image_info(image):
#     print(type(image))
#     print(image.shape)  #高宽
#     print(image.size)  #像素数据大小
#     print(image.dtype)  #
#
def video_demo():
    capture = cv.VideoCapture(0)  #0为usb摄像头
    while 1:
        ret,frame = capture.read()
        frame = cv.flip(frame,1) #1视频左右调换   0上下调换
        cv.imshow('video',frame)
        c = cv.waitKey(50)
        if c == 27:
            break

# img = cv.imread('/Users/hzh/OpenCV程序/photos/cat.png')
# cv.namedWindow('input image')
# cv.imshow('input image',img)
# get_image_info(img)
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imwrite('/Users/hzh/OpenCV程序/photos/gray.png',gray)

# cv.waitKey(0)
# cv.destroyAllWindows()

video_demo()
cv.waitKey(0)
cv.destroyAllWindows()





# img = cv.imread('/Users/hzh/OpenCV程序/photos/black.JPG')
# print(img.item(150,120,0))
# img.itemset((150,120,0),255)
# print(img.item(150,120,0))


























































































































































