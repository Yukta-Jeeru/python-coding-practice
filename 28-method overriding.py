class A:

    def show(self):
        print('in A show')

class B(A):

    def show(self):
        print('in B show')

C1=B()
C1.show()
