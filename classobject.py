class Dog:
    def __init__(self,c,nf,e):
        self.colour=c
        self.numberoffoot=nf
        self.eyes=e

    def character(self):
        print("colour of dog is:", self.colour)
        print("number of foot of dog is:", self.numberoffoot)
        print("number of eyes of dog is:", self.eyes)

obj=Dog('black',4,2)
obj2=Dog('orange',3,2)
obj3=Dog('white',2,1)

obj.character()
obj2.character()
obj3.character()

