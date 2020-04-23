"""Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
Anna Feferman"""

from random import randint  # імортуємо рандом

w = False  # заводимо змінну w
a = int(input('Input any number: '))  # користувач вводить значення а
b = int(input('Input any number: ')) # користувач вводить значення b
array = []  # створюємо порожній масив
length = int(input('Input length of the array: '))  # вводить довжину масиву
for i in range(length):
    array.append(randint(-10, 10))  # заповнюємо масив випадковими значеннями
for el in array:
    if el % a == 0 and el % b != 0: # перевіряємо умову
        w = True # змінюємо значення на true
print(array)
print(w)