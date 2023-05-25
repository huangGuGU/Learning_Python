
n1 = int(input('请输入第一个数:'))
n2 = int(input('请输入第二个数:'))

result = n1 > n2
print('n1>n2:', result)


#n1 = input('请输入第一个数:')
#n2 = input('请输入第二个数:')
#result = n1 > n2
#print('n1>n2:', result)
#如果不用int（）则无论如何都是ture，需要吧字符串变成整型才能进行比较。

money = 20000
salary = 222
print(money is salary)
#判断是否一样