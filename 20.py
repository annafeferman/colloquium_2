"""Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # масив
given = int(input('Input number: '))  # користувач вводить число
summa = 0  # зміна суми
for i in range(20):
    array.append(randint(50, 100))  # заповнюємо список рандомом від 50 до 100
print(array)
for el in array:
    if el > given:  # порівнюємо значення з тим, що вводить користувач
        summa += el  # додаємо до суми 1, якщо знайдено
        continue
print(f'Сума: {summa}')
