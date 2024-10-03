import time

def bobble_sort(ls):
    seconds = time.time()
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True
    seconds = time.time() - seconds
    return ls, seconds


def selection_sort(ls):
    seconds = time.time()
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[i] < ls[lowest]:
                ls[i], ls[lowest] = ls[lowest], ls[i]
    seconds = time.time() - seconds
    return ls, seconds

def insertion_sort(ls):
    seconds = time.time()
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = key
    seconds = time.time() - seconds
    return ls, seconds
