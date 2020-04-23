"""Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # масив порожній
new_array = []  # результуючий масив
for i in range(15):
    array.append(randint(0, 50))  # заповнюємо список рандомом
print(array)
for index in range(0, len(array), 2):  # перебираємо парні елементи
    new_array.append(array[index])  # створюємо список лише з парних елементів
print('Найбільший: ', max(new_array))  # знаходимо найбільший елемент
count = new_array.count(max(new_array))  # рахуємо скільки разів зустрівся
if count != 1:  # і визанчаємо тим самим чи він єдиний
    print('Не єдиний')
else:
    print('Єдиний')
