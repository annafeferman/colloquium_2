"""Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # масив порожній
for i in range(20):
    array.append(randint(0, 300))  # заповнюємо список рандомом
print(array)
set_array = set(array) # перетворюємо список у множину
if len(set_array) == len(array): # порівнюємо довжини множини і списку
    print('Елементи не повторюються')
else:
    print('Елементи повторюються')