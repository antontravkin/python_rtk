"""Конспект 10.10.2024"""

for animal in ['кошка','собака','хомяк','свинья','короыв']:
    if animal == 'кошка' or animal == 'собака':
        print(animal)
    else:
        print('другое')
        

#списки

L = ['Иванов Иван',182.1,1987,['#123', 1000]]
arr =[1,2,3,4]
print(L[0], L[3][1])
print(type(arr))
print(L[0:3])
L.extend([1235])
print(L)
print(L.sort)

#словарь

"""
s = {'name':'Ivan','sex':'m','age':'12',}
print(type(s))
print(s['name'])
"""

w = 'A,B,C,D'.split(',')
print(w)
A = w
print (A)
A[0] = 'test'
print(A)
print(w)       