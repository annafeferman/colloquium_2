"""Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
Anna Feferman"""

from random import randint  # імпортуємо рандом

count = 0  # змінна лічильника
array = []  # створюємо порожній список
length = int(input('Input the length of the array: '))  # довжина масиву
for i in range(length):
    array.append(randint(0, 20))  # заповнюємо рандінтом
for index in range(len(array)):
    if array[index] == index+1 and array[index] % 3 == 0:  # перевіряємо умови
        count += 1
print(array)
print(count)