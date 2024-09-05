#Checkpoint
class Hat:
    def __init__(self, kind, color, material):
        self.kind = kind
        self.color = color
        self.material = material

myObject = Hat("fedora", "brown", "felt")
#challenges A fruit festival
class Fruit:
    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size

raspberry = Fruit("circle", "sour", "small")
grape = Fruit("circle", "savory", "small")
apple = Fruit("circle", "sweet", "medium")
watermelon = Fruit("circle", "yummy", "large")
print(raspberry.kind)
print(grape.kind)
print(apple.kind)
print(watermelon.kind)
#challenge Pet store
class Pet:
    def __init__(self, shape, kind, size):
        self.shape = shape
        self.kind = kind
        self.size = size

dog = Pet("slobbery", "woofy", "big")
cat = Pet("sleepy", "meow", "lazy")
snake = Pet("noodle", "snakey", "long")