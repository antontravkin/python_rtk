"""Домашнее задание №1"""

""" Задание 1 """
try:
    number = int(input("Введите число: "))
    if number > 0:
        print("Число положительное")
    elif number < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")
except ValueError:
    print("Ошибка ввода! Введите целое число.")
   
""" Задание 2  """
try:
    number = int(input("Введите число: "))
    if number < 1 or number > 9:
        print("Ошибка ввода! Введите число от 1 до 9.")
    else:
        for i in range(1, 10):
            print(f"{number} * {i} = {number * i}")
except ValueError:
    print("Ошибка ввода! Введите целое число.")
    
""" Задание 3 """

import random
# Загадываем число от 1 до 100
random_number = random.randint(1, 100)
# Пока число не будет угадано, продолжаем игру
while True:
    try:
        # Получаем ввод пользователя
        user_input = int(input("Введите число: "))
        # Сравниваем введенное число с загаданным
        if user_input == random_number:
            print("Вы угадали!")
            break
        elif user_input < random_number:
            print("Число больше.")
        else:
            print("Число меньше.")
    except ValueError:
      print("Ошибка ввода! Введите целое число.")
