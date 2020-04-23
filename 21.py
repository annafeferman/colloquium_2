"""Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # масив порожній
given = int(input('Input number: '))  # користувач вводить число
dobutok = 1  # зміна добутку
for i in range(10):
    array.append(randint(50, 100))  # заповнюємо список рандомом від 50 до 100
print(array)
for el in array:
    if el < given:  # порівнюємо значення з тим, що вводить користувач
        dobutok *= el  # збільшуєму змінну добутку на це значення
        continue
if dobutok == 1:
    print(f'Значень менших за {given} не знайдено.')
else:
    print(f'Добуток: {dobutok}')
