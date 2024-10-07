# Модули. Способы импортирования кода.

# Main

from Module_4_lesson_2_2 import say_hi as s_h
import sys, math
import random
import tkinter
#import [path].simple_draw - path - каталог для вызова модуля

s_h()

b = 10

for path in sys.path:
    print(path)