name = input("Enter your name: ")
current_year = 2024
date_of_birth = int(input("What year you was born? "))
age = current_year - date_of_birth
print (type(name))
print (type(date_of_birth))
print (type(age))
print ("Hello, ", name)
print ("In this year you have", age, "years old")


# Variant 2

#name = input("Enter your name: ")
#current_year = 2024
#date_of_birth = input("What year you was born? ")
#age = current_year - int(date_of_birth)
#print ("Hello, ", name)
#print ("In this year you have", age, "years old")

name = input("Enter your name: ")
current_year = 2024
date_of_birth = int(input("What is your year of birth? "))
#print (type(name))
age = current_year - date_of_birth
print ("Hello,", name)
print ("You have", age, "years old in this year.")

#----------------------------

print ('Привет, я строка в нижнем, '.lower(), 'а я - в верхнем регистре'.upper())
print ('Привет, я строка в нижнем регистре, '.replace(' ', '#'))

