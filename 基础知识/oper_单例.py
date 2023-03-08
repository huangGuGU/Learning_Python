'''单例模式'''
'''开发模式'''

class Singleton:
    __instance = None
    name = 'jack'
    def __new__(cls):


        if cls.__instance is None:
            cls.__instance = object.__new__(cls) #产生一个内存地址，并把内存地址赋值给__instance

        return cls.__instance  #如果有init就return给inti

    def show(self):
        print(Singleton.name)



s = Singleton()
s1 = Singleton()

print(s)
print(s1)

s.show()
s1.show()


