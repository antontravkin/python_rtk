"""Конспект 25.03.2025"""

print('hello')

n = int(input('Введите число: '))
steps = 0

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1

print(steps)
