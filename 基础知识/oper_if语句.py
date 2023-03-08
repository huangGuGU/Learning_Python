"""
条件判断
for
跳转语句
"""
##########################################################

# print('666为用户名，输错就登陆失败')
# j = str(input('空格跳过演示:'))
# if j == ' ':
#     print('')
# else:
#     username = input('请输入用户名:')
#     if username == '666':
#         print('登陆成功')
#     if username != '666':
#         print('登陆失败')
#
#     print('-----')

##########################################################

# print('数字默认')
# j = str(input('空格跳过演示:'))
# if j == ' ':
#     print('')
# else:
#
#     num = int(input('输入数字'))
#
#     if num:
#         print('...')
#
#     if num != 0:
#         print('jjj')
        # 这两个等效

##########################################################


# print('未满18不予进入')
# j = str(input('空格跳过演示:'))
# if j == ' ':
#     print('')
# else:
#
#     age = int(input('输入年龄：'))
#     name = str(input('输入名字：'))
#     if age > 18 and name:
#         print('{}今年{}岁了'.format(name, age))
#     else:
#         print('未满18不予进入')
# 缩进统一tab
##########################################################

#
# print('选择模式')
# j = str(input('空格跳过演示:'))
# if j == ' ':
#     print('')
# else:
#     game_mode = input('选择游戏模式（1v1/2v2）：')
#
#     if game_mode == '1v1':
#         print('免费玩')
#
#     else:
#         print('开始充值')
#         money = int(input('请充值金额（100的整数）：'))
#         if money % 100 == 0:
#             money_ture = money
#             print('您已充值了:', money_ture)
#         else:
#             print('需要充值为100的整数！！！！！！！！')

##########################################################
# 随机数
# print('随机数')
# j = str(input('空格跳过演示:'))
# if j == ' ':
#     print('')
# else:
#
#     import random
#
#     print(random.randint(1, 10))

##################################################################################################################
'''elif'''
# print('多重条件判断 100-90优 90-80良 80-70及格')
#
#
# j = str(input('空格跳过演示:'))
# if j==' ':
#     print('')
# else:
#
#
#     socre = int(input('请输入成绩(0~100):'))
#     if socre>100 :
#         print('你tm在逗我？？？？？')
#     elif socre >90 and socre<= 100:
#         print('优')
#     elif socre<=90 and socre>80:
#         print('良')
#     elif socre<=80 and socre>70:
#         print('及格')
#     else:
#         print('不及格')


##################################################################################################################

'''三目运算符'''
# a = 4
# b = 5
# result = (a + b) if a < b else (b - a)
# print(result)
# 为真计算前面，为假计算后面
