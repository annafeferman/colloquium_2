"""Дані про температуру повітря за декаду листопада зберігаються в масиві.
Визначити, скільки разів температура опускалася нижче -10 градусів.
Anna Feferman"""

from random import randint  # імпортуємо рандом

temperatures = []  # масив з температурами
count = 0  # лічильник
for temperature in range(10):  # 10 оскільки "декада"
    temperatures.append(randint(-20, 7))  # заповнюємо список температур рандомом
print(temperatures)
for temp in temperatures:
    if temp < -10:  # порівнюємо температури з -10
        count += 1  # додаємо до лічильника 1, якщо знайдено
        continue
print(f"Температура опускалася нижче -10 {count} рази")
