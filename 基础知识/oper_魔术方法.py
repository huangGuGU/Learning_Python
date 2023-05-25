'''魔术方法'''
# class Phone:
#     def __init__(self):
#         self.brand = 'xiaomi'
#         self.price = 4999
#     def call(self):
#         print('self:', self.price)

# phone1 = Phone()

# phone1.call()

# phone2 = Phone()
# phone2.call()


'''repr方法'''
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
#     def __repr__(self):
#         return 'helllo'
#
#     def __str__(self):
#         return 'good'
#
#
# class Person:
#     def __repr__(self):
#         return 'hi'
#
#     def __str__(self):
#         return 'good'
#
#
#
# s = Student('lisi', 95)
# print(s)  # helllo
#
# p = Person()
# print(p)  # good


'''call方法,对象后面加括号，触发执行,把对象当成了函数。'''
# class Person:
#
#     def __call__(self, *args, **kwargs):
#         print('__call__',args,kwargs)
#
#
# p = Person()  # 执行 __init__
# p('x',{'a':10,'c':21},a=4,b=6)  # 执行 __call__


'''__del__'''


# class Student:
#     def __init__(self,name,score):
#         print('__init__方法被调用了')
#         self.name = name
#         self.score = score
#
#     def __del__(self):
#         print('__del__方法被调用了')
# s = Student('lisi',95)
# del s


'''当空间没有任何引用后就会调用del'''
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print('______del_________')
#
# p = Person('jack')
# p1 = p  # p p1 p2 的地址都是一样的
# p2 = p
# print(p1.name)
# print(p2.name)
#
# p1.name = 'tom'
# print(p.name)
# print(p2.name)
#
# del p
# print('删除p')
# del p2
# print('删除p2')
# del p1   #至此引用全部删完 调用del函数
# print('删除p1')

'''如果只有del p1 del p2 但也会触发del函数，因为程序结束后python会回收所有开辟的内存'''




# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         return self.age + other
#
#     def __sub__(self, other):
#         return self.age - other
#
#     def __mul__(self, other):
#         return self.age * other
#
#     def __truediv__(self, other):
#         return self.age / other
#
#     def __mod__(self, other):
#         return self.age % other
#
#     def __pow__(self, power, modulo=None):
#         return self.age ** power
#
#
# s = Student('zhangsan', 18)
# print(s + 1)  # 19
# print(s - 2)  # 16
# print(s * 2)  # 36
# print(s / 5)  # 3.6
# print(s % 5)  # 3
# print(s ** 2)  # 324




'''str,打印对象名的时候自动触发,原本打印对象名只会出现地址,return必须有,return后的内容就是打印对象的内容'''
# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return
#
# p = Person('tom',18)
# print(p)

'''__getitem__'''


# class DataTest:
#     def __init__(self, id, address):
#         self.id = id
#         self.address = address
#         self.d = {self.id: 1,
#                   self.address: "China"
#                   }
#
#     def __getitem__(self, key):
#         return "hello"
#
#
# data = DataTest(1, "China")
#
# print(data[24])



'''__len()__'''
# class Fib(object):
#     def __init__(self, num):
#         a, b, L = 0, 1, []
#         for n in range(num):
#             L.append(a)
#             a, b = b, a + b
#         self.numbers = L
#
#     def __str__(self):
#         return str(self.numbers)
#
#     __repr__ = __str__
#
#     def __len__(self):
#         return len(self.numbers)
#
# f = Fib(10)
# print (f)
# print (len(f))

'''__iter()__'''
# class Fib:
#     def __init__(self, max):
#         self.max = max
#     def __iter__(self):
#         print('__iter__ called')
#         self.a = 0
#         self.b = 1
#         return self
#     def __next__(self):
#         print('__next__ called')
#         fib = self.a
#         if fib > self.max:
#             raise StopIteration
#         self.a, self.b = self.b, self.a + self.b
#         return fib
# for i in Fib(3):
#     print(i)

'''__setattr__()'''
# class Fun:
#     def __init__(self):
#         self.name = "Liu"
#         self.age = 12
#         self.male = True
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#         print("*" * 50)
#         print("setting:{},  with:{}".format(key, value))
#         print("current __dict__ : {}".format(self.__dict__))
#         # 属性注册
#
# fun = Fun()