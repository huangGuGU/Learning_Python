'''
循环导入
    A:
        def test():
            f()
    B:
        def f():
            test()


'''
from 语法.user.oper_循环导入2 import func


def task1():
    print('task1')


def task2():
    print('task2')
    func()

if __name__ =='__main__':
    task1()
    task2()