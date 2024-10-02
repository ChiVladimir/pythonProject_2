# Модули и пакеты
# https://drive.google.com/drive/folders/1dQ5FCCtiVePobQ37jWmTcPH9bppXOZo3

# Subroutine

from dis import dis

def some_func():
    a = "Hello! I'm from Module 2"
    print ("Hello! I'm from Module 2")
    return a

dis(some_func)