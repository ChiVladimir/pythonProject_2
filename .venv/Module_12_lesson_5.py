# Логирование

import logging
import math


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        c = a / b
        logging.info(f'Successful divide {a}/{b}')
        return c
    except ZeroDivisionError as err:
        logging.error("Don't try to divide by zero", exc_info=True)
        return 0

def add_(a, b):
    return a * 2 + b * 3

def sqrt(a):
    try:
        c = math.sqrt(a)
        logging.info(f'take the square root {a}')
        return c
    except:
        logging.error("You cannot extract the square root", exc_info=True)
        return 0





if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO,
                        filemode='a',
                        filename='calc_py.log',
                        format='%(asctime)s | %(levelname)s | %(message)s')

    print(div(3,4))
    print(div(3,0))
    print(sqrt(4))
    print(sqrt(-5))

    # logging.debug('gf')
    # logging.info('j')
    # logging.warning('f')
    # logging.error('f')
    # logging.critical('a')