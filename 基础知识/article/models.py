class Article:
    def __init__(self,name,author):
        self.name=name
        self.author=author

    def show(self):
        print('author:{},book_name:{}'.format(self.author,self.name))

class Tag:
    def __init__(self,name):
        self.name =name
