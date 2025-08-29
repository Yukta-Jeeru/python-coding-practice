#instance method

# class student:
#
#     def __init__(self):
#         self.name='yuktha'
#
#     def greet(self):
#         print('hello',self.name)
#
# s1=student()
#
# s1.greet()

#class methods
class student:
    school='xyz'

    @classmethod
    def getschool(cls):
        print('This is my school:',cls.school)

student.getschool()
