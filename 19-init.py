class computer:

    def __init__(self,cpu,size):
        self.cpu=cpu
        self.size=size

    def config(self):
        print(f'The features are {self.cpu} cpu & {self.size} ram')


com1=computer('i5','16gb')
com1.config()  #2nd way

