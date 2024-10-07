# Классы и объекты


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        i = 1
        while i <= self.number_of_floors:
            if self.new_floor > self.number_of_floors:
                print(f'Этаж номер {new_floor} - не существует')
                break
            if self.number_of_floors >= self.new_floor >= i:
                print(f'Этаж номер {i}')
            i += 1


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
