# class A:
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
# class B(A):  # B inherits A
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
# b1 = B()
# b1.feature1()  # Inherited from A
# b1.feature3()  # Defined in B


#multi-level

class A:
    def feature1(self):
        print("Feature 1 working")

class B(A):  # B inherits A
    def feature2(self):
        print("Feature 2 working")

class C(B):  # C inherits B (and indirectly A)
    def feature3(self):
        print("Feature 3 working")

c1 = C()
c1.feature1()  # From A
c1.feature2()  # From B
c1.feature3()  # From C

a1=A()
a1.feature1()