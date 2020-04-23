"""Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # порожній список
r = False  # ставимо флаг
for i in range(15):
    array.append(randint(2, 7))  # заповнюємо рандінтом
print(array)  # виводимо список
for index in range(len(array)):
    if array[index] == array[index - 1] == array[index - 2]:  # перевіряємо три елементи один за іншим
        r = True  # присвоюємо значення істини
print(r)
