"""列表推导式"""


'''格式：【表达式 for 变量 in 旧列表】or [表达式 for 变量 in 旧列表 if 条件]'''


'''case1:过滤长度小于等于3的人名'''

names = ['tom','bob','jack','abc','sdadsa','Jj','A','a','Afkjsdnf','Okkkkk','2131232']
result = [name for name in names if len(name)>3 ]
print(result)

'''
功能类似于：
def func(name):
    newlist=[]
    for name in names:
        if len(name)>3:
            newlist.append(name)
    return newlist


'''
'''然后首字母大写'''

result = [name.capitalize() for name in result ]
print(result)






'''case1:1-100能被3整除的，放入列表'''
newlist = [num for num in range(1,101) if num%3 ==0]
print(newlist)





'''case2:[(0,1),(0,3),(0,5)....(0,9),(2,1)....(10,9)]'''


'''1'''
# list =[]
# for i in range(0,5):
#     for j in range(0,5):
#          if i %2==0 and j%2 ==1:
#             list.append((i,j))
# print(list)


'''2'''
# list = [(i,j) for i in range(5) for j in range(5) if i%2 ==0 and j%2==1]
# print(list)





'''

list1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]---->[3,6,9,5]

'''
# list1 = [[1,2],[4,5,6],[7,8,9,6,1,2,9],[1,3,5],[1]]
# newlist = [i[-1] for i in list1 ]
# print(newlist)



'''case3:如果薪资大于5000加200，低于5000加500'''
# dict1 = {'name':'tom','salary':1000}
# dict2 = {'name':'jj','salary':500}
# dict3 = {'name':'kk','salary':3000}
# dict4 = {'name':'zz','salary':10000}

# list1 = [dict1,dict2,dict3,dict4]
# nlist = [person['salary']+200  if person['salary']>5000 else  person['salary']+500 for person in list1  ]
# print(nlist)

'''改变字典里得值'''
# for person in list1:
#     if person['salary'] >5000:
#         person['salary'] += 200
#     else:
#         person['salary'] += 500
# print(list1)

# nlist = [{'name':person['name'],'salary':person['salary']+200}  if person['salary']>=5000 else {'name':person['name'],'salary':person['salary']+500}  for person in list1  ]
# print(nlist)



###########################################################################################################################################

'''集合推导式(类似列表推导式，但比列表推导式多了一个去重)'''

# list1 = [1,2,1,3,5,2,1,8,9,7,7,7,7]
# set1 = {x+1 for x in list1 if x>=5}
# print(set1)


'''字典推导式'''

# dict1={'a':'A','b':'B','c':'C','d':'C'}
# ndict = {value:key for key,value in dict1.items()}
# print(ndict)
