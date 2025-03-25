"""Конспект 17.10.2024"""

# Функции
import os


def hour_to_sec(hour, min, sec):
    return hour * 60 * 60 + min * 60 + sec


print(hour_to_sec(0, 5, 50))

account = {'username': 'azatyakupov', 'online': True, 'friends': 400,
           'username': 'azatyakupov', 'online': True, 'friends': 400,
           'username': 'azatyakupov', 'online': True, 'friends': 400}
print(account['username'])

print('test')

account1 = {'username': 'user1',
            'online': False,
            'friend': 0 }

print(account1)

account2 = {'username': 'user1',
            'username': 'user',
            'online': False,
            'points' : 723}

print(account2)

print(account2.items())

for key, value in account2.items():
    print(key, value)
account2 ['points'] = 345
account2 ['username'] = 'Anton'
print(account2) 
