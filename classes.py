class MySecondClass:
    favorite_number = 41
    def print_number(number):
        print(number)
        
MySecondClass.favorite_number
MySecondClass.__dict__['favorite_number']
MySecondClass.print_number(41)

class muesli:
    grains = 120
    def milk(self):
        return self.grains * 0.1
    
granola = muesli()
granola.price = 10

granola.taste = 2

getattr(granola, 'price')

class jumper:
    def __init__(self, size = "L", color = "brown", material = "wool"):
        self.size =  size
        self.color = color
        self.material = material
        
my_jumper = jumper(material = "polyester")
my_jumper.material


class cave:
    def __init__(self, size, location):
        self.size = size
        self.location = location
    def resize(self, size):
        self.size = size
        
smaugs_cave = cave(size = "large", location="Middle-earth")
smaugs_cave.resize.__self__
smaugs_cave.resize('small')
smaugs_cave.size

cave.resize(smaugs_cave, 'enormous')

smaugs_cave

class House:
    def __init__(self, size, color):
        self.size = size
        self.color = color
    
    def build_expansion(self, new_size):
        self.size = new_size