'''闭包
1外部函数定义了内部函数
2外部函数有返回值
3返回值是内部函数，不能加（）
4内部函数引用外部函数变量值
def 外部函数：
    。。。
    def 内部函数（）：
        。。。。
        return 内部函数

'''

#
# def func1():
#
#     b = 100
#     def inner_func():
#         a =10
#         print(a,b)
#     return inner_func
#
# x = func1()
# x()
# print(x)


# def func(a,b):
#     c= 10
#     def inner_funce():
#         print(a+b+c)
#     return inner_funce
#
# ifunc = func(1,2)
#
# ifunc()

'''闭包的使用'''
'''
1保存返回返回闭包时的状态（外层函数变量）


'''

# def func(a,b):
#     c= 1
#     def inner_funce():
#         s = a+b+c
#         print(s)
#     return inner_funce
#
# ifunc = func(1,2)
# ifunc1 = func(3,8)
#
# ifunc()
# ifunc1()


'''计数器'''

# def generate_count():
#     container = [0]
#
#     def add_one():
#         container[0] += 1
#         print('当前是第{}次访问'.format(container[0]))
#
#     return add_one
#
# counter = generate_count()
#
# counter()
# counter()
# counter()


# def func():
#     a = 10
#     def func1():
#         b = 5
#         print(a+b)
#
#     def func2():
#         func1()
#         c = 3
#
#         print(a+c)
#         return c
#
#     return func2
#
# s = func()   #s = func2
# print(s)
#
# t = s()    #func2()
# print(t)


'''
装饰器
1 函数A作为参数出现的，函数B接受函数A作为参数
2 有闭包的特点
'''

# def func(number):
#     a =100
#
#     def inner_func():
#         nonlocal a
#         for i in range(number):
#             a+=1
#         print('修改后的值',a)
#
#     return inner_func
#
# f = func(5)
#
# f()


'''
1 house被装饰函数
2 将被装饰函数作为参数传给装饰器decorate
3 执行装饰器函数
4 将返回值赋值给house
'''

# '''定义一个装饰器'''
# def decorate(func):#house赋值给func
#
#     print('wrapper外层打印')
#     def wrapper():
#         func()
#         print('刷墙')
#         print('铺地板')
#
#     print('warpper finish')
#     return wrapper    #return出来赋值给house
#
#
# '''使用装饰器'''
#
#
# @decorate   #执行到此时，将要装饰的函数也就是底下的函数，作为参数给decorate，house赋值decorate
# def house():
#     print('我是毛坯房')
#
#
# '''调用函数'''
# house()  #这时候house为wrapper
#
# print(house)  #可以看出 house和wrapper地址一致
#
#



'''地址引用'''
# def test():
#     print('test')
#
# def func(f):   #f =test
#     print(f)   #<function test at 0x7fb2482503a0>
#     f()   #test
#     print('*****')
#
#
# func(test)








'''带有参数'''
# def decorate(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrapper
#
#
# @decorate
# def f1(num):
#     print('f1',num)
#
# @decorate
# def f2(name,age):
#     print('f2',name,age)
#
# @decorate
# def f3(*list1,**k):
#     print('f3',list1,k)
#
#
# f1(2) #执行的是wrapper
# f2('hzh',23)
# jj=[1,2,3,4]
# f3(jj,room = 203, floor =2)






# def decorate1(func):
#     print('1start')
#     def wrapper1():
#         func()
#         print('铺地板')
#
#     print('1end')
#     return wrapper1
#
#
# def decorate2(func):
#     print('2start')
#     def wrapper2():
#         func()
#         print('刷墙')
#
#     print('2end')
#     return wrapper2
#
#
# '''就近原则，先使用decorate2'''
# @decorate1
# @decorate2
# def house():
#     print('毛坯房')
#
# house()



'''带参数装饰器需要为三层'''

# def decorate_out(a):   #第一层：负责接收装饰器参数
#
#     def decorate_inner(func):  #第二层：负责接收函数
#
#         def wrapper(*args,**kwargs):    #第三层：负责接收函数的参数
#             print('刷{}面'.format(a))
#             func(*args,**kwargs)
#
#         return wrapper   #返回出来第三层
#
#     return decorate_inner    #返回出来第二层
#
# @decorate_out(10)
# def house(time):
#     print('我{}日期拿到了房子，是毛坯房'.format(time))
#
# @decorate_out(100)
# def street():
#     print('xx路')
#
# house('2020-1-1')
# street()