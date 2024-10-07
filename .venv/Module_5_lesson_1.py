# Классы и объекты

class Human:
    def __init__(self, name):
        self.name = name

den = Human('Den')
max = Human('Max')



print (type(den))
print (type(5))
print(den == max)
print(den is max)
print(id(den), id(max))
print(den.name, max.name)