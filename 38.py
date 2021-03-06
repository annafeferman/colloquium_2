"""Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
Anna Feferman"""

from random import randint  # імпортуємо рандом

north, south, east, west = [], [], [], []  # створюємо порожні списки для кожного напряму
count = 0  # лічильник
for i in range(10):  # заповнюємо кожний список рандінтом
    north.append(randint(1, 14))
    south.append(randint(1, 14))
    east.append(randint(1, 14))
    west.append(randint(1, 14))

winds = {'North': north, 'South': south, 'East': east, 'West': west}  # об'єднуємо в словник для зручності використання
for el in south:
    if el > 8:  # перевіряємо чи швідкість більша за 8
        count += 1  # збільшуємо лічильник, якщо так

print(f'Швидкість південних вітрів: {south}')
print(f'Пвденний вітер більший за 8 м\с був {count} разів.')
