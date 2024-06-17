from art import tprint

class Hello:
    def __init__(self, word):
        self.word = word

    def tprint(self):
        tprint(self.word)


from class1 import MyClass
myobj = MyClass('Bear')
myobj.tprint()
