'''面向对象'''

'''所有类名需要首字母大写，多个单词使用驼峰式'''
'''
class 类名[(父类)]：
    属性：特征
    方法：动作
'''
# class Phone:
#     brand = 'huawei'
#
# print(Phone)
#
# hzh = Phone()
# print(hzh)
#
# hzh.brand = 'iphone'
# print(hzh.brand)
#
#
# jj = Phone()
# print(jj.brand)


'''定义类和属性'''
# class Student:
#     #类属性
#     name ='jj'
#     age = 2
#
# #使用类：创建对象   类名（）
# jj = Student()
# print(jj.name)
#
# kk = Student()
# print(kk.name)
# kk.name = 'kk'
# print(kk.name)
#
#
# Student.name ='xx'
# yy = Student()
# print(yy.name)


'''
类中方法:
    普通方法:
        def 方法名（self[]）:
            pass



    类方法
'''

# class Phone:
#     brand = 'xioami'
#     price = 4999
#     type = 'mate 80'
#
#     def call(self):
#         print('self:', self)
#
#         print('finding address_list')
#         for person in self.address_list:
#             print(person.items())
#
#         print('calling...')
#         print('留言', self.note)  # self在变化，所以拿到的note也不一样
#
#
# phone_1 = Phone()
# phone_1.note = 'I am phone111111'
# phone_1.address_list = [{'hzh': '213123123'}, {'jj': '12334453'}, {'kk': '42341231'}]
# print(phone_1.brand)
# phone_1.call()
#
# print('*' * 30)
#
# phone_2 = Phone()
# phone_2.note = 'I am phone2222222'
# phone_2.address_list = [{'nancy': '213123123'}, {'joy': '12334453'}, {'jam': '42341231'}]
# print(phone_2.brand)
# phone_2.call()

'''带参数'''
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eat(self,food):
#         print('{}在吃{}'.format(self.name,food))
#
# P1 =Person('hzh',19)
# P1.eat('肉')


'''猫'''

# class Cat:
#     type = '猫'
#
#     def __init__(self,nickname,age,color):
#         self.nickname = nickname
#         self.age = age
#         self.color = color
#
#     def eat(self,food):
#         print('{} love eating {}'.format(self.nickname,food))
#
#     def catch_mouse(self,color):
#         print('{} is catching a {} mouse'.format(self.nickname, color))
#
#     def sleep(self,hour):
#         if hour<5:
#             print('is time to sleep')
#         else:
#             print('is time for fun')
#
#     def show(self):
#         print('the information of the ',self.nickname)
#         print('color:',self.color)
#         print('age:',self.age)
#
# Cat1 =Cat('tom',2,'yellow')
# Cat1.eat('shit')
# Cat1.catch_mouse('green')
# Cat1.sleep(6)
# Cat1.show()


'''
类方法

1.定义需要装饰器@classmethod
2.类方法中参数不是一个对象，而是类
3.类方法中只能使用类属性
4.类方法中不可以使用普通方法

作用：
因为只能访问类属性和类方法，所以可以在对象创建之前，如果需要完成一些动作（功能），不依赖于对象
'''

# class Dog:
#
#
#
#     @classmethod
#     def test(cls):
#         print('x')
#
#
#
# Dog.test()

'''
静态方法
1.需要装饰器@staticmethod
2.静态方法无需传递参数
3.也只能访问类的属性和方法
4.加载时机同类方法


总结：
类方法 静态方法
相同：
    1只能访问类属性方法，对象的无法访问
    2都可以通过类名调用访问
    3都可以在创建对象之前使用，不依赖于对象
不同：
    1装饰器不同
    2类方法有参数，静态方法没有
    
普通方法与两者区别
不同：
    1没有装饰器
    2普通方法依赖于对象
    3要创建了对象才能使用普通方法
'''


# class Person:
#     __age = 18
#
#
#     @classmethod
#     def update_age(cls):
#         cls.__age = 20
#         print('修改后', cls.__age)
#
#     @staticmethod
#     def test():
#         print('静态方法')
#
# Person.update_age()
# Person.test()


