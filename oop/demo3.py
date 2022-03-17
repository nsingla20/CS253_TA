class Fruit:
    def __init__(self, color, size):
        self.name='fruit'
        self.color=color
        self.size=size
    def show(self):
        print(f'I am a {self.name}, I am {self.color} and of size {self.size}')

orange=Fruit('orange',8)
orange.show()

orange.size=9

del orange.size
