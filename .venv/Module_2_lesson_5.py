for i in 1, 2, 3, 3, 5, 4:
    print ("Ура!", i)

for i in "Hello":
    print ("Ура!", i)

list_ = ['one', 'two', 'three', 'four']
for i in list_:
    if i == 'two':
        list_.remove(i)
        print("Тадам!", i)
print(type(list_), list_)

for i in range(5): # 0, 1, 2, 3, 4
    print ("Брдзынь!", i)
    if i in range(len(list_)):
        list_[i] = ' :( '
        break
    print (list_[i])
print ("Hello!")
list_2 = [2, 3, 4, 5, 1]
sum_ = 0
for i in range(len(list_2)):
    sum_ += list_2[i]
print (sum_)

#start/end/step (11) - конец последоательности, (1, 11) - начало и конец последовательности, (1, 11, 2) + шаг последовательности

for i in range (1, 11): #i star from 1, then 2, 3, 4....
    for j in range (1, 11):  #j star from 1, then 2, 3, 4....
        print (f'{i} x {j} = {i * j}')

dict_ = {'a':1, 'b':11, 'c':111}
for i in dict_:
    print (i, dict_[i])
for i, k  in dict_.items():
    print(i, k)
