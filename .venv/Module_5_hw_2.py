# Классы и объекты


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        label = str(f'Название: {self.name}, кол - во этажей: {self.number_of_floors}')
        return label

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1.__str__())
print(h2.__str__())

print(h1.__len__())
print(h2.__len__())

