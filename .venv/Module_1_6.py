#Dictionary
print ("------------- Dictionary -------------")
print ()
my_dict = {'Bob':1980,
           'Rob':1990,
           'Snob':2000}
print (" Dictionary:          ", my_dict)
print (" Key", '\033[1;3;37;40mRob:             \033[0m', my_dict.get('Rob', 'The key is not defined'))
print (" Key", '\033[1;3;37;40mDrob:            \033[0m', my_dict.get('Drob', 'The key is not defined'))

my_dict.update ({'Shnob':1970,
                'Drob':1900})
a = my_dict.pop('Rob')
print(" Deleted value:       ", 'Rob ', a)
print (" Modified dictionary: ",my_dict)

#Set
print ()
print ("------------- Set -------------")
print ()
my_set ={0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 'Apple', (1, 2, 3), 5, 6}
print(" Set:          ", my_set)
my_set.add ('Banana')
my_set.add (10)
my_set.discard(0)
print(" Modified set: ",my_set)