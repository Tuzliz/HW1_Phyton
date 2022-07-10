# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, 
# и проверяет, является ли этот день выходным.
day_of_week = ['Пн - 1','Вт - 2', 'Ср - 3','Чт - 4', 'Пт - 5','Cб - 6', 'Вс - 7']
print(day_of_week)
num = int(input('Enter day of week: '))
if num >= 6 and num <= 7:
    print(f'{num} - > this is working day')
else:
    num <= 5
    print(f'{num} - > this is weekend')    
