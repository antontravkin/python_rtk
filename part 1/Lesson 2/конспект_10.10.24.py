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

"""Кортедж"""
#не изменяются
my_tuple = (1, 2, 3, "hello", True)
print(my_tuple[1])

tuple2 = ('Python','Anna',123,1.3)

for i in enumerate(tuple2):
    print ('tuple2[{0[0]}] : {0[1]}'. format(i))

tuple1 = (1,2,3,4,5)
tuple2 = (elem for elem in tuple1)

print(next(tuple2))
print(next(tuple2))
print(next(tuple2))
print('______')
tuple1 = (1,2,3,4,5,3)
tuple2 = (elem for elem in tuple1 if elem%2==0)
print(next(tuple2))
print(next(tuple2))
print('______')
print(tuple1.count(3))
print('______')
print(tuple1.index(3))

"""Множества"""

# Создаем множество 
my_set = {"Яблоко", "Апельсин", "Банан"} 
# Печатаем содержимое множества
print(my_set)

# Генератор множества
a = {i*10 for i in range(5)}
# Печатаем содержимое множества
print(a)

set1 = ('pop','pop','sock', 'soul','rock', \
    'disco', 'soul',)
print(set1) 

A = set (['яблоко' , 'апельсин' , 'лимон ' ])
A.add('банан')
A.remove('яблоко')
print(A) 
if 'апельсин' in A:
    print ('мы его купили!')
    
bag1 = { 'молоко', 'сыр', 'яблоко', 'хлеб'} 
bag2 = { 'молоко', 'сыр'}

#J = |bag1 intersect bag2| / |bagi union bag2|
# 1 / 6 = d (bag, bag2)

intersection = bag1 & bag2
print(intersection)
bag1.difference(bag2)
print(bag1)
bag2.difference(bag1)
print(bag2)

bag1.intersection (bag2)
print(bag1)

bag1.union(bag2)
print(bag1)

print(bag1.issuperset(bag2))
print(bag2.issuperset(bag1))

d = {'имя': 'Иван', 'фамилия': 'Иванов'}
print(d)