# s1='abc'
# s2="abc"
# s3='''abc'''
# print(id(s1),id(s2),id(s3))
# print(s1 ==s2)
# print(s1 is s2)
# print(s1 ==s3)
# print(s1 is s3)
# '''==比较内容 ，is 比较地址'''
#
# s1 = input('请输入：')
# s2 = input('请输入：')
# print(s1 ==s2)#ture
# print(s1 is s2)#false
#iput 输入底层做了处理，地址不一样，常量is是ture




##################################################################################################################



# name ='steven'
# result = 'st' in name  #返回 t f
# print(result)



##################################################################################################################



'''[] [:]'''


# filename = 'picture.png'
# print(filename[5])
# print(filename[0:5])
# print(filename[:7])
# print(filename[3:])
# print(filename[-5:-2])
# print(filename[-3:])
# print(filename[:-3])

'''[::]'''


# name ='1234567'
# print(name[::-1])#第三位为-1就是从右向左取值，
# print(name[-1:-8:-1])


##################################################################################################################


'''大小写相关'''


# message = 'she is a beautiful girl!'
# msg = message.capitalize() #将字符串第一个字符串变成大写形式
# print(msg)
#
#
# msg = message.title() #每个单词首字母大写
# print(msg)
#
# result = msg.istitle()
# print(result)
#
#
# msg = message.upper() #全部大写
# print(msg)
#
# result = msg.lower() #全部小写
# print(result)






##################################################################################################################


#案例：验证码
'''1'''

# s='QWERtyuiopasdfghjklzxcvbnm1234567890'
#四个随机数
# import random
# ran1 = random.randint(0,len(s)-1)
# ran2 = random.randint(0,len(s)-1)
# ran3 = random.randint(0,len(s)-1)
# ran4 = random.randint(0,len(s)-1)
#
# code = s[ran1]+s[ran2]+s[ran3]+s[ran4]
# print(code)



'''2'''
# import random
# s='QWERtyuiopasdfghjklzxcvbnm1234567890'
# i=0
# code = ''
# for i in range(0,4):
#     ran = random.randint(0,len(s)-1)
#     code += s[ran]
# print(code)

'''3'''
# import random
# s='QWERtyuiopasdfghjklzxcvbnm1234567890'
# i=0
# code = ''
# while i<4:
#     ran = random.randint(0,len(s)-1)
#     code = s[ran]
#     i +=1
#     print(code,end='')



##################################################################################################################


'''查找与替换'''
#find() rfind() lfind() index() rindex() lindex() replace()


# s1 = 'index lucy lucky goods'

# result = 'R' in s1
# print(result)
# position = s1.find('l')
# print(position)   #-1代表没找到，否则返回第一个找到的字母位置


# p = s1.find('l',7,13)
# print(p)





# ur1 = 'https://img.alicdn.com/imgextra/i1/32wqeqws.jpg'
# p = ur1.rfind('/')
# q = ur1.rfind('.')
# print(p)
# print('图片名字',ur1[p+1:q])
#
# q = ur1.rfind('.')
# print('格式',ur1[q+1:])
# '''index()与find()一致，index()如果找不到会报异常'''



'''替换'''

# s1 = 'index lucy lucky goods'
#
# s2 = s1.replace(' ','#',2)
# print(s2)


##################################################################################################################


'''字符串内建函数：encode decode'''



# msg = '上课啦！'
# result = msg.encode('utf-8')
# print(result)
#
# m = result.decode('utf-8')
# print(m)


'''
startswith() 判断是否是xxx开头
endswith() 判断是否是xxx结尾
返回true false
'''

# filename = '笔记.doc'
# result = filename.endswith('txt')
# print(result)


'''isalpha()  isdigit()'''

# s= 'abcd6'
# result = s.isalpha()
# print(result)
#
# s = '123'
# result = s.isdigit()
# print(result)
#

'''数字累加三次得出结果，如果不是数字就不算在累加次数里'''
# i = 0
# sum = 0
# while i <3:
#     num = input('请输入数字{}:'.format(i+1))
#     if num.isdigit():
#         sum +=int(num)
#         i +=1
#     else:
#         print('不是数字，请重新输入！')
#
# print(sum)



##################################################################################################################


'''join,'''

#
# new = ' '.join('abc')
# print(new)
#
#
# list1 = ['a','b','9','c']
# result = ''.join(list1)
# print(result)



'''split count'''
s = 'asd sd dds  sad'
n = s.split(' ',4)
t = s.count(' ')
print(n,t)
































