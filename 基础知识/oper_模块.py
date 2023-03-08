# import module_calculation as ca
#
# list1 = [1,2,3]
#
# result = ca.sum_list(*list1)
# print(result)
#
#
#
#
# print(ca.num)
#
# c = ca.Cal(10)
#
# c.test(20)
#
#
# ca.Cal.test1()#类方法


'''单独使用其中一个功能'''
# from module_calculation import sum_list,num
#
# print(sum_list(*list1),num)

'''全部使用，如果想限制获取的内容，可以再模块中使用__all__ = [*可以访问内容]'''
# from module_calculation import *
# c = Calculation(10)  #__all__里没有Calculaiton,所以不可用


# test(10)

###################################################################################################################################

'''文件夹，包'''
'''一个包可以放多个模块'''

# from article import models
# a = models.Article('hzh','活着')
# a.show()
#
# from article.models import Article
# a = Article('hzh','活着')
# a.show()
#
#
# from user.models import User
#
# user = User('hzh',123)
# user.login('hzh',1234)


'''
__init__文件
导入包时，默认执行的文件
1.把一些初始化参数，变量，类定义在init文件中
2.此文件中函数，变量等的访问只需要通过（包名.函数）


'''
# import user
#
# user.create_app()
#
# from user.models import User
# u = User('hzh',123)
# u.login('hzh',123)


from user import *  # 需要在__init__里方__all__[]来设置可以导入的模块

###################################################################################################################################
'''sys'''

# import sys
# print(sys.path)
# print(sys.version)
# print(sys.argv)


'''time'''

import time

#
# t = time.time()  # 获取时间戳
# print(t)
# # time.sleep(2)  #定时2秒
# s = time.ctime(t)  # 把时间戳变成字符串
# print(s)
#
# t = time.localtime(t)  # 将时间转成元组
# print(t)
# print(t.tm_hour)  # 小时
# print(t.tm_min)
#
# t = time.mktime(t)  # 转换成时间戳，数字只保留整数
# print(t)
#
# s = time.strftime('%Y-%m-%d  %H:%M:%S')  # 元组时间转换为字符串
# print(s)

'''datetime'''

import datetime

# d = datetime.date(2021, 6, 18)
# print(d.day)
# print(time.time())
# print(datetime.date.ctime(d))
# print(datetime.date.today())
# timedel = datetime.timedelta(hours=3)  #时间差
# print(timedel)
#
# now=datetime.datetime.now()  #得到当前时间
# print(now)
# result = now-timedel
# print(result)



'''random'''
# import random
# ran = random.random()
# print(ran)   #0-1随机小数
#
#
# ran = random.randrange(1,10) #取不到10
# print(ran)
#
#
# list1= ['a','b','c','x','y']
# ran=random.choice(list1)
# print(ran)


# random.shuffle(list1)   #随机排序
# print(list1)



# def func():
#
#     code =''
#     for i in range(4):
#         ran1 = random.randint(0,9)
#         ran2 = chr(random.randint(65,90))
#         ran3 = chr(random.randint(97,122))
#
#         r = random.choice([ran1,ran2,ran3])
#
#         code+=str(r)
#     print(code)
#
# func()


'''哈希'''
# import hashlib
#
# #加密
# msg = '一起吃饭'
# md5 = hashlib.md5(msg.encode('utf-8'))
#
# print(md5.hexdigest())







































































































































































































































































































































