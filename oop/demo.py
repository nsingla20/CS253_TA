class Fruit:
    def __init__(self,color,size):
        self.name='fruit'
        self.color=color
        self.size=size    

    def show(self):
        print("this is "+str(self.name)+" of color"+str(self.color))

apple = Fruit('red',3)
print(apple.name)
print(apple.color)
print(apple.size)

apple.show()
