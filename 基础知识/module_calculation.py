
# __all__ = ['sum_list','num']
def sum_list(*args):
    sum = 0
    for i in args:
        sum += i
    return sum



num = 100

class Cal:
    def __init__(self,num):
        self.num = num
        print('init',self.num)

    def test(self,number):

        print('调用了class',number)

    @classmethod
    def test1(cls):
        print('ca类方法')


def test(num):
    print('test',num)

if __name__ =='__main__':
    test(10)

test(10)#会自动执行