#subroutine

def divide(first, second):

    result = float()
    if second == 0:
        result = str("Error")
    if second != 0:
        result = first / second

    return result

