class car:

    wheels=4

    def __init__(self):
        self.mil=10
        self.comp='BMW'

c1=car()
c2=car()

c1.mil=8

car.wheels=5


print(c1.mil,c1.comp,c1.wheels)
print(c2.mil,c2.comp,c2.wheels)
