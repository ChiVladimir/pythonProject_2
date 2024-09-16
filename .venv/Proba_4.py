#food = ["apple", "coconut", "banana"]
#print (food [0])
#food [0] = "peach"
#print (food)
#food.append(True)
#print (food)
#food.extend(["string", 2])
#print (food)
#food.remove("banana")
#print (food)
#print ("coconut" in food)
#print ("coconut" not in food)
#print (food[0:2:3])

tuple_ = 1, 2, 3, 4, 5
tuple_2 = (1, 2, 3, False, "String", True)
tuple_3 = ([1, 2, 3, 4, 5])
# tuple_ [0] = "peach" | TypeError: 'tuple' object does not support item assignment
print (tuple_)
print (tuple_2)
print (tuple_3)
print (tuple_2[3])

tuple_4 = 1, 2, 3, 4, 5
list_4 = [1, 2, 3, 4, 5]
print (tuple_4.__sizeof__())
print (list_4.__sizeof__())

tuple_5 = ([1, 2], 3)
print (tuple_5)
tuple_5 = ([1, 2], 3) + (4, 5)
tuple_5[0][1] = 3
print (tuple_5)

tuple_6 = (1, 2, 3) * 4
print (tuple_6)