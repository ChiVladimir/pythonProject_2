# Задание "Свой YouTube"

import time
import sys

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return f'hash(self.password)'

    def __int__(self):
        return self.age

class Video:

    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *files):
        for kino in files:
            if kino.title not in [video.title for video in self.videos]:
                self.videos.append(kino)

    def get_videos(self, kinopoisk: str):
        kinopoisk_ = list()
        for video in self.videos:
            if kinopoisk.lower() in video.title.lower():
#                print('yes', video.title)
                kinopoisk_.append(video.title)
        return kinopoisk_

    def watch_video(self, title, duration):
        if get_videos(title) in self.title:
            if self.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
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


ur = UrTube()
u1 = User('Bob','qwerty', 20)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
"""
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