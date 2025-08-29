class computer:
    def __init__(self):
        self.name='yuktha'
        self.age=22

    # def update(self):
    #     self.age=40

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1=computer()   #constructor
c2=computer()

c1.name='Ram'
c1.age=40

if c1.compare(c2):
    print('they are same')
else:
    print('they are different')

# c1.update()


print(c1.name)
print(c2.name)

print(c1.age)
print(c2.age)