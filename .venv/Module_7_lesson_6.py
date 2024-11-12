# Файлы в операционной системе.

import os

from gevent.testing.testrunner import print_list

print('current directory - ', os.getcwd())
if os.path.exists('First'):
    os.chdir('First')
else:
    os.mkdir('First')
print('current directory - ', os.getcwd())

if os.path.exists('Second/Third/Fourth'):
    print('current directory - ', os.getcwd())
    os.chdir('Second/Third/Fourth')
    print('current directory - ', os.getcwd())
else:
    os.makedirs(r'Second/Third/Fourth')
print(os.listdir())
for i in os.walk('.'):
    print((i))
os.chdir('../.')
for i in os.walk('.'):
    print((i))
os.chdir('..')
for i in os.walk('.'):
    print((i))
os.chdir('..')
for i in os.walk('.'):
    print((i))
os.chdir('..')
print('current directory - ', os.getcwd())
files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(dirs)
print(files[6], '\n')
#os.startfile(files[6]) #does not work on iOS/Linux
print(os.stat(files[6]))
print(os.stat(files[6]).st_size)
os.system('pip install random2')
os.system('pip install --upgrade pip')