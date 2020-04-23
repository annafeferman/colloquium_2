"""Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []
for i in range(15):
    array.append(randint(-20, 20))  # заповнюємо список рандомом
print(f'{array}\n'
      f'Мінімальне значення: {min(array)}')  # виводимо мінімальне значення
