class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self,username,password):
        if self.username == username and self.password == password:
            print('登录成功')
        else:
            print('登录失败')

