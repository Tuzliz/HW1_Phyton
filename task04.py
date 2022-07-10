#  Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
num_of_quaters = ['quater -1', 'quater - 2', 'quater - 3', 'quater -4']
print(num_of_quaters)
num_of_quater = input('Enter number of quater: ') # проверка на ввод числа 
if num_of_quater.isdigit():
    print('Is a namber')
else:
    print('Not a number')
#num_of_quater = ' '                                #второй вариант проверки для себя
# while num_of_quater.isdigit() == False:
#    num_of_quater = input ('Введите номер четверти: ')
#print('Номер четверти: {}'.format(num_of_quater))
def f(num_of_quater):
    if num_of_quater == 1: 
        return 'x > 0, y > 0'
    elif num_of_quater == 2:
        return 'x > 0, y < 0'
    elif num_of_quater == 3: 
        return 'x < 0, y < 0' 
    else:
        return 'x < 0, y > 0'       

print(f'Points belongs to the range: {f(num_of_quater)}')
