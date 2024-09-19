def say_hello():
    print ('Hello!')
say_hello()

def say_hello(name):
    print ('Hello! ', name)
#name = input(' Enter your name:')
#say_hello(name)
say_hello('Bob')

import random
def lottery():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(tickets)
    return win
win = int((lottery() + lottery()) / 2)
print (win)

import random
def lottery(mon, thue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2
win1, win2 = lottery('mon', 'thue')
print (win1, win2)

def test(a = 2, b = True):
    print (a, b)

test ()
test (False, 'ok')
test ([1, 2])
test (*[1, 2])
