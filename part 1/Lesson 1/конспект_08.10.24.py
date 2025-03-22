"""Конспект 08.10.2024"""

import sys

a = 5
b = 2
if a > b:
    print('a больше b')
    if a == 5:
        print('a = 5')
    elif (a == b):
        print('a=b')
    else:
        (f' а не равно {a}')
else:
    print('ошибка')

print("конец программы")

for i in range(1, 2):
    print (i*3)
    if (i == 5):
        print(350)
        
for i in range(1, 6):
    print('Итерация № ' +str(i)) 

colors = ['красный','сини','зеленый','желты','черный',]
print(colors)
for color in colors:
    print(color)

for i, color in enumerate(colors):
    print(i, color)

print('-------') 
x, y = 6,7
print(str(x) +' '+ str(y))

dates = ['2000','2010','2032','2005','2080']
i = 0
year = 0
while(year!='2005'):
    year = dates[i]  
    i+=1
    print(year)
    
count = 0
while(count <= 100):
    print(count)
    if(count > 15):
        break #continue #pass
    count+=1
print('Конец программы')

for i in range(x):
    print ((x-1) * ' ' + i * '+')

for i in range(x):
    if i < 6:
        print (i * ' *')
    else:
        print ((x-1) * ' *')
        
total = 0
for number in range(5):
    total += number
print(total)

for number in range(5, 0, -2):
    print(number)
    
print('__________________')

"""Исключения"""

""" • ZeroDivisionError - деление на ноль.
• AttributeError - объект не имеет данного атрибута (значения или метода).
• NameError - не найдено переменной с таким именем.
• SystemError - внутренняя ошибка.
• TypeError - операция применена к объекту несоответствующего типа. 

try:
    Операторы 
except Исключение:
    Обработка исключения 
else: # выполняется, когда в try не возникло исключения
    Действия
finally: # выполняется в любом случае
    Действия
"""
""" try:
    a = float(input())
    b = float(input())
    print(a/0)
except ValueError:
    print('Ошибка конвертауции чисел')
except ZeroDivisionError:
    print('нельзя дел на ноль')
else:
    print('если') """
#finally:
#    print('Конец')
    
#Оператор raise позволяет вызывать собственные исключения.
"""
a = -9
if a < 0:
    raise Exception("Число должно быть положительным")
"""

""" class MyException(Exception):
    pass
try:
    number1 = int(input("Введите первое число: ")) 
    number2 = int(input("Введите второе число: "))
if number2 == 0:
    raise MyException("Второе число не должно быть 0")
except ValueError:
    print("Введены некорректные данные")
except MyException:
    print("Завершение программы") """
    
try:
    for i in range (3,-3,-1):
        print(1/i)
except Exception as e:
    print('какая то ошибка ' + str(e))
    

    for i in range (3,-3,-1):
        try:
            print(1/i)
        except ZeroDivisionError as e:
            print(0)
f= None
try:
    f = open('test.txt', 'r')
    print(f.readlines())
except IOError:
    print('Ошибка файла')
finally:
    if f:
        f.close
print('конец программы')