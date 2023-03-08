
'''
匿名函数

lambda 参数1，参数2：运算

'''




# s = lambda a,b:a+b
# t = s(3,4)
# print(t)
# s1 = lambda a,b:a*b
# t = s1(2,5)
# print(t)




# def func(x,y,f):
#     print(x,y)
#
#     s = f(x,y)
#     print(s)
#
# func(1,2,lambda a,b:a+b)



'''找a的最大值'''
# list2 = [{'a':12,'b':20},{'a':20,'b':10},{'a':120,'b':200},{'a':41,'b':220}]
# m = max(list2,key = lambda x:x['b'])
# print(m)



'''map,对列表中的某些元素进行操作时候会用到'''
# list1 = [1,2,3,4,5]
# result = map(lambda  x:x+2,list1)
# print(list(result))


'''带有判断'''
# list1 = [1,2,3,4,5]
# func = lambda x:x if x%2==0 else x+1
# result = map(func,list1)
# print(list(result))



'''reduce()对列表中的元素进行加减乘除的函数'''

# from functools import reduce
# tuple1 = (1,2,3,4,5)
#
# result = reduce(lambda x,y:x+y, tuple1)
# print(result)

# tuple2 = (1,2,3)
# result = reduce(lambda x,y:x-y, tuple2,5)
# print(result)


'''filter()'''

# dict1 = [{'name':'hzh','age':18},
#          {'name':'jj','age':28},
#          {'name':'kk','age':8},
#          {'name':'zz','age':38}]
# result = filter(lambda x:x['age']>30,dict1)
# print(list(result))
#
#
#
# dict1 = sorted(dict1,key = lambda x:x['age'])
#
# print(dict1)


'''递归函数'''

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
#
# result = sum(10)
# print(result)
