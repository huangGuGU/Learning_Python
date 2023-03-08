
#
# names =['jack','tom','lucy','jerry','man']
#
# computer_brands=[]
#
# print(id(names))
#
# print(id(computer_brands))
#
# print(names[0])
# print(names[-1])

'''可以用for'''
# for i in names:
#     print(i)

'''查询names里有没有lucy'''

# for i in range(0,len(names)):
#     if names[i] =='lucy':
#        print(i)
#

'''改'''
# i = 0
# brands = ['hp','dell','mac','呵呵']
# brands[-1] = 'HASEE'
# while 'dell' not in brands[i]:
#     i +=1
# else:
#     brands[i] = 'huawei'
# print(brands)


'''del删除'''
'''删除mac和hp'''

# brands = ['hp','dell','mac','呵呵']
#
# i = 0
# l = len(brands)
# while i<l:
#     if 'hp' in brands[i] or 'mac' in brands[i]:
#         del brands[i]
#         l -=1
#     i +=1
# print(brands)




'''删除输入的文字'''

# brands = ['hp','dell','deell','mac','huawei','delllll','ddel']
# delete = input('需要删除的文字：')
# l = len(brands)
# i = 0
# while i<l:
#    if delete in brands[i]:
#         del brands[i]
#         l-=1
#    else:
#         i +=1
# print(brands)


######################################################################################################################



# i = 0
# for w in ['goods','good','abc']:
#     print('good' in w)
#     i +=1
'''
if 让 in 判断作为一个条件表达式
 
if 'a' in ['a','b']：

for ...in
for 变量 in 字符串/列表：


'''


# if 'c' in ['a','b','c']:
#     print('j')
# else:
#     print('jj')


# j = 0
# while j <3:
#     for i in ['a','b','c']:
#         if i =='b':
#             print(j)
#             j +=1
#         else:
#             j +=1




######################################################################################################################

'''字符串切片操作'''

# list1 = ['jj','kk','aa','hehe',100,99.9]#字符能够混放
# print(list1)
#
#
# #列表支持切片
# print(list1[3])
# print(list1[3:5])#列表支持切片
# print(list1[-3:-1])
# print(list1[::2]) #支持步长
# print(list1[-1::-1])
#
# print(list1[-1::-2])
#



######################################################################################################################


'''列表的添加'''
#列表函数的使用 append extend insert
#创建一个空列表


'''append()反复末尾添加'''
# girls = ['x']
# while 1:
#     name = input('输入名字：')
#     if name =='quit':
#         break
#     girls.append(name)  # append 末尾添加 只能一个一个来
# print(girls)




'''extend'''
# girls = ['x']
# name = input('输入名字：')
# girls.extend(name)  # exend 拆分后末尾添加
# print(girls)
# call= ['asd','baa','cs']
# girls.extend(call) #extend可以一堆往里面放
# print(girls)




''' 用 + 合并'''
# girls = ['x']
# names=['y','z']
# girls= girls+names
# print(girls)



'''insert插入'''
# girls = ['x','y','z']
# girls.insert(1,'a')  #指定位置后插入
# print(girls)




######################################################################################################################


'''
产生10个随机数
将产生的随机数放在列表并打印

'''
# import random
# num = []
# for i in range(0,10):
#     ran = random.randint(0,9)
#     num.append(ran)
# print(num)




# import random
# num = []
# i =0
# while i<10:
#     ran = random.randint(0,9)
#     num.append(ran)
#     i +=1
# print(num)

######################################################################################################################
'''
产生10个

不同的

随机数
将产生的随机数放在列表并打印

'''


# import random
# num = []
# i =0
# while i<10:
#     ran = random.randint(0,9)
#     if ran in num:
#         pass
#     else:
#         num.append(ran)
#         i+=1
# print(num)




'''while无限循环，看数组长度'''
# import random
# num = []
#
# while 1:
#     ran = random.randint(0,9)
#     if len(num) < 10:
#         if ran in num:
#             pass
#         else:
#             num.append(ran)
#     else:
#         break
# print(num)

######################################################################################################################

'''
产生10个
不同的
随机数
将产生的随机数放在列表并打印

找出最大小值
'''

# import random
# num = []
# i =0
# while i<10:
#     ran = random.randint(0,1000)
#     if ran in num:
#         pass
#     else:
#         num.append(ran)
#         i+=1
# print(num)
#
# maxn = num[0]
# k=0
# minn = num[0]
# for j in num:
#     if maxn-j<0:
#         maxn =j
#
# for j in num:
#     if minn-j>0:
#         minn =j
# 
# print(maxn)
# print(minn)






'''有重复最大值，求出位置和个数'''
# import random
# num = []
# i = 0
# while i < 10:
#     ran = random.randint(0, 10)
#     num.append(ran)
#     i +=1
# print(num)
#
#
#
# #找出最大值
# maxn = num[0]
#
# minn = num[0]
# for j in num:
#     if maxn < j :
#         maxn = j
#
#
# #计算最大值个数
# w = 0
# for a in num:
#     if a == maxn:
#         w+=1
# print('最大值是：',maxn,'  ,  ''有{}个最大值'.format(w))
#
# for i in range(len(num)):
#     if num[i] == maxn:
#         print('最大值位置是：',i)
#


'''便捷的函数'''

# a=[1,23,4,123,3,322]
#
# maxn = max(a)
# print(maxn)
#
# minn = min(a)
# print(minn)
#
# he = sum(a)
# print(he)

######################################################################################################################


'''sorted排序'''
# a=[1,23,4,123,3,322]
# new_list = sorted(a)
# print(new_list)
# new_list = sorted(a,reverse=True)  #反转
# print(new_list)

'''自己排序大小'''
#
#
# #0-9打乱的数
# import random
# num = []
# k = 0
# while k < 10:
#     ran = random.randint(0, 9)
#     if ran in num:
#         pass
#     else:
#         num.append(ran)
#         k +=1
# print(num)
#
# #开始排序
#
# for i in num:
#     for j in num:
#         if i<j:



######################################################################################################################


'''数组嵌套'''
# result = [3,2] in [3,2,[3,2,1],[3,2,1,0]]
# print(result)
# result = [3,2] in [3,2,[3,9],[3,2,1,0]]
# print(result)


'''取出列表中的列表值'''
# a  = [3,2,[3,9],[3,2,1,0]]
# print(a[2][1])


# print(list(range(10,2,-2)))




######################################################################################################################

'''例题'''

'''数列结果题目'''
# a=[1,2,3,4,5,6,7,8,9]
# print(a[5:0:-1])
# print(a[3:-9:-1])
# a='123456789'
# print(a[5:0:-1])
#
# print('*'*20)
#
# a=[1,2,3,4,5,6,7,8,9]
# print(a[:5:-1])
# a='123456789'
# print(a[-1:5:-1])



'''pop remove del'''
# a=[12,2,3,43,5,63,3,3,9]
# a.remove(3)   #删除第一个匹配的值
# print(a)
#
#
# a=[12,2,3,43,5,63,12,9]
# a.pop(3)
# print(a)
# a.pop()
# print(a)
#
#
# a=[12,2,3,43,5,63,12,9]
# del a[:2]
# print(a)


'''3全删了'''
# a=[12,2,3,43,5,63,3,3,9,3,3,3,3,3]
# while 3 in a:
#     a.remove(3)
# print(a)


'''取出规定字符'''
# a = 'this is a test of python'
# b = a[a.find('test'):a.find('test')+4]
# print(b)
# c= a.find('test')
# print(c)


'''大写变小写，小写变大写'''

'''1'''
# a = 'JsadlJSDlsadhISADHLN'
# a = a.swapcase()
# print(a)

'''2'''
#错误方法
# a = 'JsadlJSDlsadhISADHLN'
# for i in a:
#     if i.islower():
#         i =i.upper()
#     else:
#         i = i.lower()
# print(a)


#正确方法
# a = 'JSSADHLNscdasdasd'
# s=''
# for i in a:
#     if i.islower():
#         s+=i.upper()
#     elif i.isupper():
#         s+= i.lower()
#     else:
#         s+=i
# print(s)




# a=[3,23,2,3,2,2,2]
# a.clear()
# print(a)

# a=['2','3','1','6']
# a.sorted()
# print(a)






'''enumerate'''
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# j = list(enumerate(seasons))
# print(j)

'''枚举列表'''
# l = ['one', 'two', 'three']
# for index, value in enumerate(l):
#     print(index, value)

'''枚举字符串'''
# for index, value in enumerate('happy'):
#     print(index, value)


'''每一项前面加一个1'''
# list1 = ['01','02','03']
# list1=["1"+i for i in list1]
# print(list1)
#
#
#
# list1 = ['01','02','03']
# list2=[]
# for i in list1:
#     list2+=["1"+i]
# print(list2)
