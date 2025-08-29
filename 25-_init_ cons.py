#case 1
# class A:
#     def __init__(self):
#         print('A init')
#
# class B(A):
#     # def func(self):
#     #     print('B init')
#     pass
#
# a1=A()

#case 2

# class A:
#     def __init__(self):
#         print('A init')
#
# class B(A):
#     def __init__(self):
#         print('B init')
#
# a1=A()
# b1=B()

#case 3
# class A:
#     def __init__(self):
#         print('A init')
#
# class B(A):
#     def __init__(self):
#         super().__init__()  #inherited properties from A
#         print('B init')
#
# b1=B()

#case 4
class A:
    def __init__(self):
        print("A init")

class B:
    def __init__(self):
        print("B init")

class C(A, B):  # Multiple inheritance
    def __init__(self):
        super().__init__()  # Calls the init of A, NOT B
        print("C init")

c1=C()
