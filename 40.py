"""Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
Anna Feferman"""

from random import randint  # імпортуємо рандом

summa = 0  # змінна суми
array = []  # створюємо порожній список
length = int(input('Input the length of the array: '))  # довжина масиву
for i in range(length):
    array.append(randint(-2, 2))  # заповнюємо рандінтом
for el in array:
    if el == 0:  # зупиняємо цикл якщо елемент дорівнює нулю
        break
    else:
        if el % 2 == 0:  # якщо ні, перевіряємо на парність
            summa += el
print(array)
print(f'Сума: {summa}')
