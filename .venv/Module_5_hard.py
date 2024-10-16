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

    def watch_video(self, kino: str):
        if self.current_user:
            for video in self.videos:
                if video.adult_mode == True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                if kino in video.title:
                    i = 1
                    while i < video.duration:
                        print(i, end=' ')
                        time.sleep(1)
                        i += 1
                    print("Конец фильма")

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user_new = User(nickname, hash(password), age)
        self.users.append(user_new)
        self.current_user = user_new



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

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


