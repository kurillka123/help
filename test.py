
'----СПИСКИ---'
#append - присоединитьнять в конец
#pop - удаляет/возвращяет элемент
#in - есть ли элемент в списке
#sort - сортирует список
#сортируем только однородные (type) списки
#for - перебирает элементы
#range - создает арифметическую прогрессию
'''
hero = [1, 4, 8, 10, 20]

counter = 0
while counter < len(hero):
    print(hero[counter])
    counter += 1

print(hero)
'''
from random import randint
ranom_digit = []
for i in range(10):
    ranom_digit.append(randint(0, 9))
print(ranom_digit)