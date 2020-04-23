"""Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
Anna Feferman"""

from random import randint  # імпортуємо рандом

rain, snow = 0, 0  # поки що опади рівні нулю
# створюємо списки для температур і к-сті опадів
temperatures = []
falls = []
for i in range(10):
    # заповнюємо списки рандінтом
    temperatures.append(randint(-10, 10))
    falls.append(randint(2, 20))
for idx in range(10):
    if temperatures[idx] < 0:  # за темп-ри нижче 0 додаємо опадки до снігу
        snow += falls[idx]
    else:  # а в протилежному випадку до дощу
        rain += falls[idx]

print(f'Дощ: {rain}\n'
      f'Сніг: {snow}')
