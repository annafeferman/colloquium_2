"""Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # порожній список
for i in range(15):
    array.append(randint(2, 7))  # заповнюємо рандінтом
print(array)  # виводимо список
for i in range(len(array)):
    if array.count(array[i]) > array.count(array[i - 1]):  # скільки разів повторюється кожне число масиву
        count = array.count(array[i]) # присвоюємо це значення в лічильник
print('Найчастіше число повторюється', count, 'разів.')
