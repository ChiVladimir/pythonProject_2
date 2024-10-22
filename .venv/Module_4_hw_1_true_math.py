#subroutine

from math import inf

def divide(first, second):
    result = float()
    if second == 0:
        return inf
    else:
        result = first / second
        return result


