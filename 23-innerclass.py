class student:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_stu(self):
        print(self.name,self.age)


    class laptop:

        def __init__(self,color,comp):
            self.color=color
            self.comp=comp

        def showlap(self):
            print(self.color,self.comp)

s1=student('Raj',22)
s1.show_stu()

s2=student.laptop('Red','HP')
s2.showlap()