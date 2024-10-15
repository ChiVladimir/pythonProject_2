# Задание "Свой YouTube"

import time
import sys

class UrTube:

    def __init__(self, *args):
        user_inp = list(args)
        self.current_user = None
        if len(user_inp) == 2:
            self.users = user_inp[0]
            self.videos = user_inp[1]

    def __log_in__(self, nickname, password):
        self.user = nickname
        self.password = hash(password)
        if user in database.data:
            if password == database.data[user]:
                self.current_user = user
                print(f'Login complete, {user}')
            else:
                print('Wrong login or password!')

    def __register__(self, nickname, password, age):
        self.user = nickname
        self.password = hash(password)
        self.age = age
        if user in database.data:
            print(f'User {user} already exist!')
        else:
            database.add_user(user, password, age)
            print(f'Login complete, {user}')

    def __log_out__(self, current_user):
        if __name__ != '__main__':
            self.current_user = None

    def __add__(self, videos):
        if videos not in self.title:
            self.videos = videos

    def __get_videos__(self, videos):
        ask_videos = lower(videos.replace(" ", ""))
        exist_videos = lower(self.title.replace(" ", ""))
        if ask_videos in exist_videos:
            print(self)
            return self

    def __watch_video__(self, title, duration):
        if get_videos(title) in self.title:
            if self.age < 18:
                print ("Вам нет 18 лет, пожалуйста покиньте страницу")
                if self.current_user == None:
                    print("Войдите в аккаунт, чтобы смотреть видео")
            for remaining in range(duration):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rComplete!            \n")
#            time.sleep(duration)
            exit()


class Video:

    def __init__(self, *args, **kwargs):
        video_bf = list(args)
        self.adult_mode = False
        if bool(kwargs.values()) == True:
            self.adult_mode = True
        time_now = 0
        self.title = video_bf[0]
        self.duration = video_bf[1]
        print(self.title, self.duration, self.adult_mode)

class User:

    def __init__(self):
        self.data = {}

    def add_user(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)


"""
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
"""