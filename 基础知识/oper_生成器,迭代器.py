'''得到生成器的方式1 列表推导式''''''列表推导式'''# list = [n*3 for n in range(8)]# print(list)'''小括号，生成器'''# g = (n*3 for n in range(10))# print(g)#'''__next__()'''# print(g.__next__())# print(g.__next__())# print(g.__next__())# print(g.__next__())# print(g.__next__())#'''next()  系统内置 next（生成器对象）'''# #每调用一次next就会产生一个元素# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))'''取值'''# g = (n*3 for n in range(10))## while 1:#     try:#         e = next(g)#         print(e)#     except:#         print('没有更多元素')#         break'''只要函数中出现yield，函数就变成了生成器'''# def func():#     n = 0#     while 1:#         n+=1#         yield n   #return n +暂停# g = func()## print(next(g))# print(next(g))# print(next(g))# print(next(g))'''斐波那契数列'''# def fib(length):#     a, b = 0, 1#     n = 0#     while n < length:#         yield a#         a, b = b, a + b#         n += 1#         return b## g = fib(8)# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))# print(next(g))'''生成器方法：    __next__()：获取下一个元素    send(value):向每次生成器调用中传值 第一次调用需要send(None)        '''# def gen():#     i = 0#     while i < 5:#         temp = yield i#         print('temp:', temp)#         i += 1#     return '没有更多的数据'### g = gen()# n0 = g.send(None)# print('n0:', n0)# n1 = g.send('hehe')# print('n1:', n1)# n2 = g.send('kk')# print('n2:', n2)'''进程 线程 协程'''# def task1(n):#     for i in range(1,n):#         print('正在搬{}砖'.format(i))#         yield None## def task2(n):#     for i in range(1,n):#         print('正在听第{}首歌'.format(i))#         yield None## g1 = task1(3)# g2 = task2(3)## while 1:#    try:#         next(g1)#         next(g2)#    except:#        pass'''迭代器可以被next（）函数调用，并且不断返回下一个值得对象称为迭代器生成器是可迭代的，也是迭代器''''''list本身不是迭代器但是可以iter一下,元组，字典，集合，字符串都需要iter'''# list1 = [1,2,3,4,5,6]# list1 = iter(list1)# print(next(list1))# print(next(list1))# print(next(list1))# print(next(list1))