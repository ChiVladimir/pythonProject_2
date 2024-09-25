# Рекурсия

def summa(n):
    if n == 0:
        return 0
    else:
        print(n + summa(n - 1))
        return n + summa(n - 1)


print (summa(5))

# стэк работает по методу LIFO

stack = []
stack.append(1)
print ('add ', stack)
stack.append(2)
print ('add ', stack)
stack.append(3)
print ('add ', stack)
stack.append(4)
print ('add ', stack)
stack.pop()
print ('delete ', stack)
stack.pop()
print ('delete ', stack)
stack.pop()
print ('delete ', stack)
stack.pop()
print ('delete ', stack)
