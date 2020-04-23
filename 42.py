"""Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
Anna Feferman"""

from random import randint  # імпортуємо рандом
import math  # імпортуємо math

count = 0  # змінна лічильника
array = []  # створюємо порожній список
length = int(input('Input the length of the array: '))  # довжина масиву
for i in range(length):
    array.append(randint(-10, 10))  # заповнюємо рандінтом
for index in range(len(array)):
    if index * index < array[index] < math.factorial(index):  # перевіряємо умови
        count += 1
print(array)
print(count)
