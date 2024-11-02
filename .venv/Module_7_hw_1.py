# Домашнее задание по теме "Режимы открытия файлов".
# Задача "Учёт товаров"



class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
#        print(self.name, self.weight, self.category)

    def __str__(self):
        a = f"{self.name}, {self.weight}, {self.category}"
        return a

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_list = file.read()
        file.close()
        return products_list

    def add(self, *products):
        _products = self.get_products()
        for product in products:
            if str(product) in _products:
                print(f'Продукт {str(product)} уже есть в магазине')
            else:
                _file = open(self.__file_name, 'a')
                _file.write(f'{str(product)}\n')
                _file.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())