"""

私有化
封装：1私有化属性 2定义公式有set 赋值 和get方法 取值

好处：1隐藏属性不被外界修改
     2可以使用set修改
     3可以使用函数来筛选
     4如果想获取具体的一个属性，可以使用get
"""

'''case1'''
# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 59
#
#     '''定义set和get方法'''
#
#     def setAge(self, age):
#         self.__age = age
#
#
#     def getAge(self):
#         return self.__age
#
#     def __str__(self):
#         return 'name：{}，age:{},socre:{}'.format(self.__name, self.__age, self.__score)
#
#
# s = Student('jj', 18)
# s.setAge(21)
# print(s)
# print(s.getAge())


'''case2 用装饰器'''

# class Student:
#     def __init__(self,age):
#
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
# s = Student(18)
# s.age = 30
# print(s.age)


'''题目'''

# class Car:
#
#     def __init__(self, name, v):
#         self.__name = name
#         self.__v = v
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return 'name:{},velocity:{}'.format(self.__name, self.__v)
#
#
# class Road:
#     def __init__(self, name, length):
#         self.__name = name
#         self.__length = length
#
#     def setName(self, name):
#         self.__name = name
#
#     def __str__(self):
#         return 'name:{},velocity:{}'.format(self.__name, self.__length)
#
#
# c = Car('Benz', 60)
# r = Road('66road', 1000)
#
# c.name = 'qq'
# print(c)
#
# r.setName('青藏高路')
# print(r)


'''class 里有 class  (has a)'''

#
# class Computer:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def __str__(self):
#         return 'brand:{},color:{}'.format(self.brand, self.color )
#
#
# class Book:
#     def __init__(self, bname, num):
#         self.bname = bname
#
#         self.num = num
#         self.__store_num = 1000 - self.num
#
#     def setBook_Num(self, num):
#         self.__store_num -= num
#
#     def getBook_Num(self):
#         return self.__store_num
#
#
# class Student:
#     def __init__(self, device, book):
#
#         self.device = device
#         self.books = []
#         self.books.append(book)
#
#     def borrow(self, book):
#         for i in self.books:
#             if i.bname == book.bname:
#                 print('has borrowed')
#                 break
#         else:
#             self.books.append(book)
#             print('done')
#             b.setBook_Num(book.num)
#
#     def show_book(self):
#         print('学生借的书:', end='')
#         for book in self.books:
#             print(book.bname + '*' + str(book.num), end='/')
#         print('剩余藏书:', b.getBook_Num())
#
#     def __str__(self):
#         return str(self.device)
#
#
# c = Computer('Apple', 'silvery')
# b = Book('高等数学', 1)
# s = Student(c, b)
#
#
# '''输入书名和个数'''
# while 1:
#     book_name = input('书名：')
#
#     if book_name == 'quit':
#         break
#     else:
#         book_num = input('接的数量:')
#         new_book = Book(book_name, int(book_num))
#         s.borrow(new_book)
#
# '''打印结果'''
# print('学生信息:', s)
# s.show_book()


'''is a'''
'''
继承：
studen,employee,doctor都属于person类
相同代码导致冗余

将相同代码提取到了person类
s，e，d继承person

class

特点：
1如果不定义init，则去父类中找init
2如果类继承了父类也需要定义自己的init，就需要在当前类的init调用父类init
3如何调用父类：
    super().__init__(参数)
    super(类名，对象).__init__(参数)
4如果父类与子类有相同的函数，则优先使用当前类
5子类的方法中也可以调用父类方法：
    super().方法名（参数)

'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
#     def eat(self):
#         print('{}正在吃饭（父类）' .format(self.name))
#
#
# class Student(Person):
#     def __init__(self, name, clazz):
#         super().__init__(name)  # super()父类对象
#         self.name = name
#         self.clazz = clazz
#
#     def study(self, course):
#         print(self.name + '正在上' + course)
#
#     def eat(self):
#         print('{}正在吃狮子头（子类）' .format(self.name))
#         super().eat() #子类中有父类
#
# class Employee(Person):
#     def __init__(self, name, wage):
#         super().__init__(name)
#         self.name = name
#         self.wage = wage
#
#
# class Doctor(Person):
#     def __init__(self, name, major, patient):
#         super(Doctor, self).__init__(name)  # 多了一个判断，Doctor是self吗
#         self.name = name
#         self.major = major
#         self.patient = patient
#
#     def __str__(self):
#         return '{}医生的专业是{}，她的病人有{}'.format(self.name, self.major, self.patient)
#
#
# '''student'''
#
# s = Student('hzh', 1324)
# s.eat()   #student里有eat函数，所以只执行student里的eat
# s.study('Math')
#
# '''employee'''
# print('-' * 50)
# e = Employee('jj', 7000)
# e.eat()
#
# '''doctor'''
# print('-' * 50)
# list1 = ['a', 'b', 'c', 'd']
# d = Doctor('kk', 'physical', list1)
# d.eat()
# print(d)

'''多重继承'''

'''case1.1  经典类'''
# class A:
#     def test(self):
#         print('aaaaa')
#
# class B:
#     def test(self):
#         print('bbbb')
#
# class C(A,B):
#     def test(self):
#         print('cccc')
#
# c =C()
# c.test()

'''case1.2'''

# class Base:
#     def test(self):
#         print('base')
#
#
# class A(Base):
#     def test(self):
#         print('aaaaa')
#
#
# class B(Base):
#     def test(self):
#         print('bbbb')
#
#
# class C(Base):
#     def test(self):
#         print('cccc')
#
#
# class D(A, B, C):
#     pass
#
#
# d = D()
# '''搜索顺序D->A->B->C'''
# d.test()
# print(D.__mro__)


'''case1.3'''
# class P1:
#     def foo(self):
#         print('p1---->foo')
#     def bar(self):
#         print('p1---->bar')
#
# class P2:
#     def foo(self):
#         print('p2---->foo')
#
# class C1(P1,P2):
#     pass
#
#
# class C2(P1, P2):
#     def bar(self):
#         print('c2--->bar')
#
# class D(C1,C2):
#     pass
#
# d =D()
# print(D.__mro__)  #寻找顺序
#
# d.foo()
# d.bar()


'''case2  新式类  P1P2有object，但在python3里没有差别，在py2里有差别'''
# class P1(object):
#     def foo(self):
#         print('p1---->foo')
#     def bar(self):
#         print('p1---->bar')
#
# class P2(object):
#     def foo(self):
#         print('p2---->foo')
#
# class C1(P1,P2):
#     pass
#
#
# class C2(P1, P2):
#     def bar(self):
#         print('c2--->bar')
#
# class D(C1,C2):
#     pass
#
# d =D()
# print(D.__mro__)  #寻找顺序
#
# d.foo()
# d.bar()


'''多态 封装 继承  ---》面向对象'''


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def feed(self, pet):
#         if isinstance(pet, Pet):  # 判断obj是否是类或子类的对象
#             print('{}喜欢养{}'.format(self.name, pet.nickname))
#         else:
#             print('这不是宠物')
#
#
# class Pet:
#
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#
# class Cat(Pet):
#     pass
#
#
# class Tiger:
#     pass
#
#
# c = Cat('tom')
# t = Tiger()
# p = Person('hzh')
# p.feed(c)
# p.feed(t)



'''子类不能继承父类的__元素'''
'''比较1'''
# class Parent:
#     def __init__(self):
#         self.x = 1
#
#     def print1(self):
#         print(self.x)
#
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.x = 2
#
#     def print(self):
#         print(self.x)
#
#
# c = Child()
# c.print1()
# c.print()
#
# '''比较2'''
# class Parent:
#     def __init__(self):
#         self.__x = 1
#
#     def print1(self):
#         print(self.__x)
#
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__x = 2
#
#     def print(self):
#         print(self.__x)
#
#
# c = Child()
# c.print1()  # 只能访问到自己的
# c.print()


