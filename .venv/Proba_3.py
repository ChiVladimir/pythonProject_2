food = ["apple", "coconut", "banana"]
print (food [0])
food [0] = "peach"
print (food)
food.append(True)
print (food)
food.extend(["string", 2])
print (food)
food.remove("banana")
print (food)
print ("coconut" in food)
print ("coconut" not in food)
print (food[0:2:3])