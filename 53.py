"""В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
Anna Feferman"""

import random  # імпортуємо рандом

choice = [0, 1, 5]  # створюємо список з потрібними значеннями
x = []
for i in range(int(input('Введіть довжину масиву: '))):  # Заповнюємо масив
    x.append(random.choice(choice))  # обираємо рандомом значення зі списку choice
print(sorted(x))  # сортуємо отриманий масив
