# Цели и задачи. Зачем нужно наследование.
# Задача "Съедобное, несъедобное"

class Animal:
    alive = True
    fed = False
    name = str

    def eat(self, food):
#        print (f"alive {self.alive}, fed {self.fed}, name {self.name}, {food.edible}, {food.name}")
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            elif not food.edible:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False

class Mammal(Animal):
    def __init__(self, name):
        self.name = name

class Predator(Animal):
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.

