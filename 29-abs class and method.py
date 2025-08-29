from abc import ABC, abstractmethod

class boss(ABC):

    @abstractmethod
    def work(self):
        pass

    def take_break(self):
        pass

class employee(boss):

    def work(self):
        print('Emp is working')

    def take_break(self):
        print('Employee took break')

C1=employee()
C1.work()
C1.take_break()

