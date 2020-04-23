"""Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
Anna Feferman"""

from random import randint  # імортуємо рандом

t = False  # заводимо змінну t
a = int(input('Input any number: '))  # користувач вводить значення а
array = []  # створюємо порожній масив
length = int(input('Input length of the array: '))  # вводить довжину масиву
for i in range(length):
    array.append(randint(-10, 10))  # заповнюємо масив випадковими значеннями
q = array.count(max(array))  # рахуємо чи повторяється максимальне значення масиву
if max(array) < a and q == 1:
    t = True  # привласнюємо значення істина при збереженні всіх умов
print(array)
print(t)
