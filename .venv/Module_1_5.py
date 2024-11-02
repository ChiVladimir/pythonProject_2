immutable_var = (1, 2, 3, False, "String", True)
print (immutable_var)

# immutable_var [0] = "peach"
#     ~~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 2, 3, "apple", "coconut", "banana"]
print (mutable_list)
mutable_list [3] = "peach"
print (mutable_list)
mutable_list.append(True)
print (mutable_list)
mutable_list.extend(["string", 2])
print (mutable_list)

immutable_var_2 = ([1, 2], 3)
print (immutable_var_2)
immutable_var_2 = ([1, 2], 3) + (4, 5)
immutable_var_2[0][1] = 3
print (immutable_var_2)