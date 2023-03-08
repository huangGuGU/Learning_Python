"""异常"""
#
# def chu(a,b):
#     return a/b
#
# x = chu(1,0)
# print('x')


'''异常处理

try:
    可能异常的代码
except：
    如果有异常执行的代码
finally：
    无论是否有异常都会执行的代码

'''


# def func():
#     try:
#         n1 = int(input('第一个数字:'))
#         n2 = int(input('第二个数字:'))
#         div = n1/n2
#         print(div)
#     except ValueError:
#         print('必须输入数字')
#     except ZeroDivisionError:
#         print('分母不能为0')
#
# func()


'''Exception'''
# def func():
#     try:
#         n1 = int(input('第一个数字:'))
#         n2 = int(input('第二个数字:'))
#         div = n1/n2
#         print(div)
#     except ValueError:
#         print('必须输入数字')
#     except ZeroDivisionError:
#         print('分母不能为0')
#     except Exception as err:
#         print('出错啦',err)
#
#
# func()



'''else'''
'''如果需要有else，那么try里不能有return'''
# def func():
#     try:
#         n1 = int(input('第一个数字:'))
#         print(n1)
#         # return 1
#     except ValueError:
#         print('必须输入数字')
#
#     else:
#         print('数字输入完毕!')  # 没有异常才执行
# func()



'''case4'''
# def func():
#     stream = None
#     try:
#         stream = open(r'/Users/hzh/Desktop/C/3.txt')
#         container = stream.read()
#         print(container)
#         return 1
#     except Exception as err:
#         print(err)
#         return 2
#
#     finally:
#         print('finally')
#         if stream:
#             stream.close()
#         return 3
# x= func()
# print(x)

'''抛出异常raise'''


'''注册用户名必须为6位'''

def register():
    username = input('输入名字:')
    if len(username)<6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名：',username)

try:
    register()
except Exception as err:
    print(err)
    print('注册失败')
else:
    print('注册成功')

































































































































































