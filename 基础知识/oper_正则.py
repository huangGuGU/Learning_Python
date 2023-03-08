import re

# msg = 'abcdefg'
# pattern = re.compile('abc')
# result = pattern.match(msg)  #match是从头开始匹配，如果匹配成功就返回一个值
# print(result)


'''使用re模块'''

# s = 'abcde'
# result = re.match('cd',s)
# print(result)
# #
# #
# #
# result = re.search('cd',s)   #search可以不从头开始搜索
# print(result)
# print(result.span()) #span为匹配的位置
#
# print(result.group())  #提取匹配的内容部分


# s='123aqwe28fas'
# result = re.search('[0-9][a-z]',s)  #search 只找一个
# print(result.group())
#
# result = re.findall('[0-9][a-z]',s) #findall全部搜索
# print(result)


'''用户名可以是字母或者是数字，不能是数字开头，长度必须6位以上'''
# username = 'admin001'
# result = re.match('[a-zA-Z]\w{5,}',username)
# print(result)
#
# username = 'admin001%%'
# result = re.match('[a-zA-Z]\w{5,}$',username) #如果需要判定到结尾就需要加$
# print(result)


# msg = 'y7kwjena2938vjnka88a'
#
# result = re.findall('[a-z][0-9]+[a-z]',msg)
# print(result)


'''分组'''
# 匹配0-100数字

# n = '31'
# result = re.match(r'[0-9]?\d$|100$',n)
# print(result)

'''
(word1|word2|word3)  区别  [abc]
或者是word1或word2或word3   或者是a或者是b或者是c


'''

# email = '32904042@qq.com'
# result = re.match(r'\w{5,20}@(163|123|qq)\.(com|cn)$',email)
# print(result)

'''爬虫'''

# msg = '<html>abc&*^%<html>'
# msg1 = '<ht>ab(c<ht>'
#
# result = re.match(r'<(\w+)>(.+)<(\w+)>$',msg)
# print(result.group(2))
#
#
# # number
# result = re.match(r'<(\w+)>(.+)<\1>$',msg1)  #\1代表与group(1)一致
# print(result.group(2))


'''起名'''

# msg = '<html><h1>abc<h1><html>'
#
# result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)<(?P=name2)><(?P=name1)>',msg)
#
# print(result)


'''替换'''
# result = re.sub(r'\d+','90','x=99,y=100')
# print(result)
#
#
#
# def func(temp):
#     num = temp.group()
#     num1 = int(num)+1
#     return str(num1)
#
# result = re.sub(r'\d+',func,'x=99,y=100')
# print(result)
#



'''熟悉group（）里面涵盖什么'''
# m = re.match('(\w+) (\w+) (\w+)', "Isaac Newton physicist")
#
# print(m.group(0))
#
# print(m.group(1))
#
# print(m.group(2))
#
# print(m.group(3))
#
# print(m.groups())
