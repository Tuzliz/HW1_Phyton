# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка.

x = int(input('Enter fist point x: '))
y = int(input('Enter second point y: '))
if x != 0 and y != 0:
    print(f'Points: x = {x};  y = {y}')
else:
    print('error')  
    # как написать, чтобы после ошибочного ввода 0, код дальше не выполнялся?  
def f(x,y):
    if x > 0 and y > 0:
        return 'quater 1'
    elif x > 0 and y < 0:
        return 'quater 4'  
    elif x < 0 and y < 0:
        return 'quater 3'  
    else: 
        return 'quater 2'  

print(f'Point belongs to the {f(x,y)}')

