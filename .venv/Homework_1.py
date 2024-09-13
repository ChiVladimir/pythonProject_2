example = 'Топинамбур'
print (example)
print (example[0])
print (example[-1])
print (example[5:10])
print (example[::-1])
print (example[1:10:2])

#----------------------

Quantity_of_completed_HW = 12
Quantity_of_hours_spent = 1.5
Course_name = 'Python'
Time_4_one_task = Quantity_of_hours_spent / Quantity_of_completed_HW

print ('\033[1;3;37;40m Курс: ', Course_name, ', всего задач: ', Quantity_of_completed_HW, ', затрачено часов: ', Quantity_of_hours_spent, ', среднее время выполнения ', Time_4_one_task, ' часа.', sep='')

#----------------------