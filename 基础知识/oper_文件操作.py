"""文件操作"""
import os

'''open(file.mode)'''

# stream = open(r'/Users/hzh/Desktop/未命名.txt')  #返回值是一个流

# container = stream.read()  #read()读取流里的东西
# print(container)

# result = stream.readable()   #判断是否可读
# print(result)
#
# result = stream.readline(3)
# print(result)

# result = stream.readlines()  #保存在列表中
# print(result)


'''如果是图片则不能使用默认的读取方式，mode=‘rb’'''

'''write,
mode是w

方法： 每次都会把原来的内容给清空然后再写入内容
    write（内容）
    writelines()没有换行效果

mode是a（append）
    不会把原来的内容清空，内容在后面追加'''

# stream = open(r'C:\Users\HZH\Desktop\hello.txt','w')
# s ='''
# 你好：
#     我叫hzh
# '''
# result = stream.write(s)
# print(result)
# stream.write('jj')
# stream.writelines('hehhehe')  #没有换行
# stream.close()


'''文件复制'''
'''
原文件
目标文件
with结合open使用可以自动释放资源

'''

# with open(r'C:\111pypypyp\1.png','rb') as stream:
#     container = stream.read()
#
#     with open(r'C:\2222pypypy\1.png','wb') as wstream:
#         wstream.write(container)
#
# print('文件复制完成')


'''模块'''

# with open(r'C:\111pypypyp\123123123.png','rb') as stream:
#     container = stream.read()
#     file = stream.name
#     n = file.rfind('\\')
#     filename = file[n+1:]
#     path = os.path.dirname(__file__)
#
#
#     '''1'''
#     path1 = os.path.join(path,filename)  #join返回拼接后的新路径
#     '''2'''
#     # path1 = path+r'\1.png'
#
#
#     with open(path1,'wb') as wstream:
#         wstream.write(container)
#
# print('文件复制完成')


'''通过相对路径找到绝对路径'''

# path = os.path.abspath('aa.txt')
# print(path)
#
#
# path = os.getcwd()#获取工作目录类似于os.path.dirname(__file__)
# print(path)


# path = "F:/Zi Liao/python程序/语法/file oper.py"
# result = os.path.split(path)
# print(result)
# print(result[1])#获取到了文件名
#
# result = os.path.splitext(path)  #找的扩展名
# print(result)
# print(result[1])
#
#
# result = os.path.getsize(path)  #返回文件大小单位字节
# print(result)


# all = os.listdir(r'C:\Program Files (x86)')   # 返回指定目录下的所有文件和文件夹保存到列表
# print(all)


# f = os.mkdir(r'C:\2222pypypy\p232')   #创建文件夹
# print('完成')


# d = os.rmdir(r'C:\2222pypypy\p232')  #删除指定文件夹
# print('完成')


# os.remove(r'C:\2222pypypy\p23\aa.txt') #删除指定文件


'''删除指定文件夹得所有文件'''
# path = r'C:\2222pypypy\p23'
# all = os.listdir(path)
# for file in all:
#     os.remove(os.path.join(path,file))
# else:
#     os.rmdir(path)
# print('删除成功')


'''文件复制'''

import os

path = r'C:\p1'
save_path = r'C:\p2'

'''定义函数'''


def copy(path, save_path):
    if os.path.isdir(path) and os.path.isdir(save_path):

        img_list = os.listdir(path)
        for img in img_list:
            img_path = os.path.join(path, img)
            save_img_path = os.path.join(save_path, img)

            with open(img_path, 'rb') as f1:
                Img = f1.read()
                with open(save_img_path, 'wb') as f2:
                    f2.write(Img)
        else:
            print('复制完毕')
    else:
        print('路径错误')


copy(path, save_path)


'''文件复制（case：文件中有文件）'''

# import os
# path = r'C:\p1'
# target_path = r'C:\p2'
#
# '''定义函数'''
# def copy(path,target_path):
#     if os.path.isdir(path) and os.path.isdir(target_path):
#
#         filelist = os.listdir(path)
#
#         for file in filelist:
#             file_path = os.path.join(path,file)
#
#             '''判断是否为文件夹'''
#             if os.path.isdir(file_path):
#
#                 '''是文件夹就开始创建新的目标文件夹并迭代'''
#                 target_path_inner = os.path.join(target_path,file)
#                 os.mkdir(target_path_inner)
#                 copy(file_path,target_path_inner)
#
#             else:
#                 '''如果不是文件夹就直接复制'''
#                 with open(file_path,'rb') as rstream:
#                     container = rstream.read()
#
#                     target = os.path.join(target_path,file)
#                     with open(target,'wb') as wstream:
#                             wstream.write(container)
#         else:
#             print('复制完毕')
#
# copy(path,target_path)
