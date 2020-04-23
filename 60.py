"""Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # порожній список
array_copy = array  # копія списку
array_2 = []  # додаткові списки (2 і 3)
array_3 = []
for i in range(10):
    array.append(randint(0, 7))  # заповнюємо рандінтом
print(array)  # виводимо список
for el in array_copy:
    if array_copy.count(el) > 1:  # перевіряємо чи числа повторюються
        if el in array_2:
            continue
        else:
            array_2.append(el)  # додаємо їх в окремий список
for el in array_2:
    array_3.append(array.count(el))  # рахуємо к-ть чисел з нового списку в вихідному
print(max(array_3))  # виводимо результат
