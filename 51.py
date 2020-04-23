"""Дан одновимірний масив а. Сформувати новий масив, який складається
тільки з тих елементів масиву а, які перевищують свій номер на 10. Якщо таких
елементів немає, то видати повідомлення.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # масив порожній
new_array = [] # результуючий масив
for i in range(10):
    array.append(randint(0, 50))  # заповнюємо список рандомом
print(array)
for index in range(len(array)):
    if (array[index] - index) > 10:  # перевіряємо умову
        new_array.append(array[index])  # додаємо до лічильника 1, якщо знайдено
        continue
print(new_array)