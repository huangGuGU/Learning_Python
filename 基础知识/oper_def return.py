

'''def'''
# import random
# def generate_random():
#     for i in range(10):
#         ran = random.randint(1,20)
#         print(ran)
# generate_random()


'''带参数'''
# import random
# def generate_random(number):  #number为形参
#     for i in range(number):
#         ran = random.randint(1,20)
#         print(ran)
# generate_random(6)  #6为实参



# def add(a,b):
#     sum = a+b
#     print(sum)
# add(3,4)
# add(5,7)


'''

定义一个登录函数，参数是username，password
函数体：
判断两个参数是否输入正确，正确就登陆成功，否则打印登录失败

'''

# def login(username,password):
#     for i in range(3):
#         if username == 'abc' and password =='123':
#             print('进入系统')
#             break
#         else:
#             print('进入失败')
#             username = input('用户名：')
#             password = input('密码：')
#     else:
#         print('账户锁定')
#
# username = input('用户名：')
# password = input('密码：')
# login(username,password)



'''找出列表最大值'''

# def maxnumber(list):
#     maxi = list1[0]
#     for j in range(len(list1)):
#         if maxi < list1[j]:
#             maxi = list1[j]
#     print(maxi)
#
#
# list1=[]
# for i in range(3):
#     num = input('输入数字：')
#     list1.append(num)
# maxnumber(list1)

'''isinstance判断类型'''
# list1=[1,23,4,1]
# if isinstance(list1,list):
#     print('是的')
# else:
#     print('不是')

'''可变变量的细节问题'''
# list1 = [1,3,5,8,9,0]
# list2 = list1
# list1.remove(5)
# print(list2)




'''参数数量不确定可以使用*（1）'''
# def add(*args):
#     print(args)
#
# add()
# add(1,2,3,4,51)
# add(1,2,3)
# add(1,)
#
#
#
# def sum(*args):
#     sumnumber = 0
#     if len(args) > 0:
#         for i in args:
#             sumnumber +=i
#         print(sumnumber)
#     else:
#             print('请输入值')
#
# sum(1,2,3,4,1,2,3,14)
# sum()
# sum(1,)



'''参数数量不确定可以使用*（2）'''
# def sum(name,age,*args):
#     sumnumber = 0
#     if len(args) > 0:
#         for i in args:
#             sumnumber +=i
#         print('%s的%s累加和为:%s'%(name,age,sumnumber))
#     else:
#             print('请输入值')
#
# sum('hzh',1,2,3,4)



'''参数数量不确定可以使用*（3）'''
# def sum(name,age,*args):
#     sumnumber = 0
#     print('%s %s岁就知道，'%(name,age),end='')
#     if len(args) > 0:
#         for i in args:
#             sumnumber += i
#             print(i,'+ ',end='')
#         print('=',sumnumber)
#     else:
#         print('请输入值')
#
# sum('hzh',18,1,4,5,1,3)



'''关键字参数'''

# def add(a,b=10):
#     result = a+b
#     print(result)
#
#
# add(5)


'''字典关键词'''


# def fun(**k):
#     print(k)
#
# fun(a=5,b=2)


'''fun里面dict1必须要**'''
# def fun(**k):
#     print(k)
#
#
# dict1 = {'hzh':18,'zyy':19,'kyy':20}
# fun(**dict1)





# dict1 = {'001':('x',18),'002':('y',19),'003':('z',30)}
#
# def fun(myname,**persons):   #有关键字但又不知道有多少，所以用**persons
#     if isinstance(persons,dict):
#         values = persons.values()
#         for name,age in values:
#             print('{}喜欢{},ta的年龄是{}'.format(myname,name,age))
#
# fun('hzh',**dict1)




def bb(a,b,*c,**d):
    print(a,b,c,d)

'''1'''
# dict1 = {'x':1,'y':2,'z':3}
# bb('haha','666',2,39,**dict1)
'''2'''
# bb('haha','666',2,39,'asknda',21,j=1,k=2,v=3)



# def func(a,*l,**dict):
#     print(a,l,dict)
#
# t=(1,2,3,4,5)
# l = [2,5,8]
# dict1 = {'1':'a','2':'b','3':'c'}
#
# func(1,l,**dict1)
# func(1,*l,**dict1)
# func(1,*t,**dict1)
#
#
#
#
#
# def func(a,l,dict):
#     print(a,l,dict)
#
# t=(1,2,3,4,5)
# l = [2,5,8]
# dict1 = {'1':'a','2':'b','3':'c'}
#
# func(1,l,dict1)
# func(1,t,dict1)





'''*和没有*'''
# def func(*l):
#     print(l)
#     for i in l:
#         print(i)
# t=['x','y','z']
# func(*t)
#
#
# def func(l):
#     print(l)
#     for i in l:
#         print(i)
# t=['x','y','z']
# func(t)




'''返回值  将函数中运算的结果通过return扔出来'''


# def add(a,b):
#     result =a+b
#     return result,100
'''只要return 就需要一个值来接住，这里是x'''
# x,y= add(2,8)
# print(x,y)





'''global'''


# name ='x'
#
# def func():
#      global name
#      name+='y'
#      print(name)
# func()





'''可变的就不需要加global'''
# list1 =[1,2,3]
# def func():
#
#      list1.append(4)
#      print(list1)
# func()


'''内部函数
1.可以访问外部变量
2.内部函数可以修改外部函数可变类型变量，list1
3.内部函数修改全局不可变变量时，需要贼内部函数申明global
内部函数修改外部函数不可变变量，要在内部函数申明nonlocal


'''

# def func():
#     n = 100
#     list1 = [3,6,9,4]
#     def inner_func():
#         nonlocal n
#
#         for index ,i in enumerate(list1):
#             list1[index]= i+n
#
#         list1.sort()
#         n +=100
#     inner_func()
#     print(list1)
#     print(n)
#
# func()



# a = 10
# def func1():
#
#     b = 100
#     def inner_func():
#         global a
#         nonlocal b
#         c = 2
#         b +=2
#         a += 2
#         print(a,b,c)
#
#
#
#     inner_func()
#     print(locals())  # 查看当前函数中，申明的内容有哪些，以字典形式返回
#     print(globals())
# func1()
























































































