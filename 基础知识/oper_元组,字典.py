'''

元组只能看和查，不能增删改
'''

# t2 = ('hello',)#要加逗号，否则不是元组类型
# print(type(t2))
#
# t2 = ('hello')
# print(type(t2))
#
# t2 = ('aa','bb')
# print(type(t2))





# list = [1,2,34,5,6546,]
# t3 = tuple(list)
# print(t3)

'''查询和列表一样，可切片'''
# print(t3[0])
# print(t3[::-1])
#
# '''max min'''
# print(max(t3))
# print(min(t3))
#
# '''sum'''
# print(sum(t3))
#
# '''求长度'''
# print(len(t3))

'''元组中自带的函数 index(),count()'''

# print(t3.count(2))
# print(t3.index(5))#找出5的位置，没有就报错



'''拆包'''
# t1 = (4,7,3)
# a,b,c = t1
# print(a,b,c)



'''变量个数与元祖个数不一致时'''
# t1 = (2,5,8,9,7)
# a,*b,c = t1
# print(a,c,*b)

#
# a,c,*b = t1
# print(a,c,b)
#
#
# t1 = (9,)
# a,*b = t1
# print(a,b) #*b代表未知个数，如果多个那就把多个放入b




###################################################################################################################################

'''字典'''




'''



列表     元组      字典
[]       ()       {}
list     tuple    dict
element  element  kye:value


'''




# dict1 = {}   #空字典 常用
# dict2 = dict() #空字典
# dict3 = {'ID':'1234214234124','name':'tom','age':18}





'''错误的'''
# dict4 = dict(('name','tom'))
# print(dict4)

# dict4 = dict((['name','tom',12],['age',18]))
# print(dict4)


# dict4 = dict((['name','tom'],['age']))
# print(dict4)


'''正确的才能变为字典'''
# dict4 = dict((['name','tom'],['age',18],['heh',19]))
# print(dict4)

'''字典的增删改查'''


'''增'''
#格式 dict6[key] = value

# dict6 = {}
# dict6['brand'] = 'huawei'
# print(dict6)




'''改'''
# dict6 = {'brand':'huawei'}
# dict6['brand'] = 'mi'
# print(dict6)


'''查'''
# dict1 = {'1':'x','2':'y','3':'z'}
# print(dict1['2'])



'''找考试分数大于90分的人'''

# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# for i in dict2: #遍历结果是key
#     print(i)



'''字典里的函数 items() values() keys()'''


'''items()'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# for key,value in dict2.items():
#     # print(key,value)
#     if value >=90:
#         print(key)

'''values()'''
dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# allscore = 0
# result = dict2.values()
# print(result)
#
# for score in dict2.values():
#     allscore += score
#     print(allscore)
# average = allscore / len(dict2)
# print(average)

for score in dict2.values():
    print(score)
scores = dict2.values()
totle =  sum(scores)
print(totle)


'''keys()'''
'''判断人名在不在字典'''

'''1'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# names = dict2.keys()
# print(names)
# for name in names:
#     print(name)
#
# if '李三' in names:
#     print('在')
# else:
#     print('不在')

'''2'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# print('李三S' in dict2) #in 可以判断元素有没有在key中出现
#
#
# print(dict2['李三'])


'''get()'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# print(dict2.get('ss'))  #get如果取不到值不会报错，返回None
# print(dict2.get('李三'))
#
# #get(key,default)
# print(dict2.get('ss',99))  #get如果取不到值不会报错，返回None，如果后面有值，会把后面的值赋值给前面的值,并返回后面的值


'''删除'''
'''del'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# del dict2['李三']
# print(dict2)

# dict2.remove('李三')#没有这样的函数
# print(dict2)

'''pop'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# result = dict2.pop('李三s','x')
# print(dict2,result)

'''popitem()'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# result = dict2.popitem()#删除末尾一个
# print(dict2,result)

'''clear'''
# dict2 = {'詹三':100,'李三':70,'王三':90,'赵三':10,}
# result = dict2.clear()
# print(dict2,result)



'''其他内置函数'''

'''update（）'''
# dict1 = {0:'tom',1:'jack',2:'lucy'}
# dict2 = {0:'lily','4':'ruby'}
#
# result = dict1.update(dict2)
# print(result)
# print(dict1)


'''fromkeys()'''
# list = ['a','b','c']
# new_dict = dict.fromkeys(list,10)
# print(new_dict)


























































