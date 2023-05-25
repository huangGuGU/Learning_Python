

# s1= set() #空集合


"""快速排序去重"""
# list1=[3,5,1,2,2,1,4]
# s1 = set(list1)
# print(s1)


'''增删改查'''

# s1.add('hello')
#
# s1.add('小坠器')
#
# s1.add(18)
#
# print(s1)

'''update()'''
# t1 = ('x','y','z')
# s1.update(t1)
# print(s1)

'''add(元组)'''
# t1 = ('x','y','z')
# s1.add(t1)
# print(s1)



'''删除 pop clear remove discard'''

# list1 = [1,47,58,3,2,7,33,4]
# s1 = set(list1)
# s1.discard(212)
# print(s1)



'''

1产生一个1-20的随机数，取出里面的重复项
2键盘输入一个元素，将此元素从不重复的集合中删除

'''

# import random
# s1 = set()
# for i in range(20):
#     ran = random.randint(1,20)
#     s1.add(ran)
# print(s1)
# num = int(input('输入一个数字：'))
# s1.discard(num)
# print(s1)



'''符号操作  in == ！=与之前一样'''


'''+ * - | &'''


set2 = {1,2}
set3 = {1,2,3}

print(set3 -set2)
# print(set2 -set3)

# print(set3 &set2)

# print(set3 |set2)

# print(set3 ^set2)





################################################################################################################################




'''列表转字典的要求'''
# list1 = [('12',1),(12,'sa')]
#
# dict1 = dict(list1)
# print(dict1,type(dict1))


'''字典变列表，只取字典中的key'''
# dict1 = {'age':18,'name':'jj'}
# print(list(dict1))

