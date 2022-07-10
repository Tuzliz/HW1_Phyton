#  Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('x,y,z - first expression')
for x in range(2):
    for y in range(2):
        for z in range(2):
            result = not x and not y and not z
            print(result)
print ('x,y,z - second expression')           
for x in range(2):
    for y in range(2):
        for z in range(2):
            result2 = not(x or y or z)
            print(result2)
if result == result2:
    print('Equality - True')
else: 
    print('Equality - False')                