name = "Vladimir"
print ("Hello, " + name)

print (("Hello, " + name + "! ") * 5)

print (name[0])
print (name[-1])
print (name[0:4])
print (name[0:7:2])
print (name[:4])
print (name[::2])
print (name[::-1])
#-------------------
name = "Antonius"
print ("Hello, " + name)

print (("Hello, " + name + "! ") * 5)

print (name[0])
print (name[-1])
print (name[0:4])
print (name[0:7:2])
print (name[:4])
print (name[::2])
print (name[::-1])

Date_Of_Birth = "September, 28"
print ("Date Of Birth: " + Date_Of_Birth)
DateOfBirth = "July, 29"
print ("Date Of Birth: " + DateOfBirth)

#-----------------------
name = "Urban"
print (name, type(name))
name = 5
print (name, type(name))
name = 5.5
print (name, type(name))
name = [1, 2]
print (name, type(name))

age = 30
new_age = '30'
print (age + new_age) #TypeError: unsupported operand type(s) for +: 'int' and 'str'