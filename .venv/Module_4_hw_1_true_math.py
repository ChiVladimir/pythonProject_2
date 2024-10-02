#subroutine

from math import inf

def divide(first, second):
    result = float()
    if second == 0:
        return inf
    if second != 0:
        result = first / second
        return result


