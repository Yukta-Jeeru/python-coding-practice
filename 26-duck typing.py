#duck typing

class pycharm:

    def editor(self):
        print('This is pycharm editor')
        print('Ok end')

class Myeditor:

    def editor(self):
        print('This is myeditor')
        print('Ok end')

class laptop():

    def code(self,ide):
        ide.editor()


ide=pycharm()

l1=laptop()
l1.code(ide)