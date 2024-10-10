# Дополнительное практическое задание по модулю 5

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержащий атрибуты: логин и пароль (с подтверждением)

    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    user = User(input("Enter username   : "),input("Enter password   : "),input("Re-Enter password: "))
    database.add_user(user.username, user.password)


# def calculate_structure_sum(data):
#
#     for_sum = []
#     result = int()
#     if isinstance(data, dict):
#         data =  list(zip(data.keys(), data.values()))
#     for i in range(0, len(data)):
#
#         if isinstance(data[i], int):
#             for_sum.append(data[i])
#
#         if isinstance(data[i], str):
#             for_sum.append(len(data[i]))
#
#         if isinstance(data[i], tuple):
#             for_sum.append(calculate_structure_sum(data[i]))
#
#         if isinstance(data[i], list):
#             for_sum.append(calculate_structure_sum(data[i]))
#
#         if isinstance(data[i], dict):
#             for_sum.append(calculate_structure_sum(data[i]))
#
#         if isinstance(data[i], set):
#             for_sum.append(calculate_structure_sum(tuple(data[i])))
#
#     result = sum(for_sum)
#
#     return result
#
#
# data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
# result = calculate_structure_sum(data_structure)
# print(result)