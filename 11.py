"""Дані про температуру води на Чорноморському узбережжі за декаду
вересня зберігаються в масиві. Визначити, скільки за цей час було днів, придатних для
купання.
Anna Feferman"""

from random import randint  # імпортуємо рандом

temperatures = []  # масив з температурами
swimming_temp = int(input('Input temperature for swimming: '))  # користувач вводить температуру для плавання
count = 0  # лічильник
for temperature in range(10):  # 10 оскільки "декада"
    temperatures.append(randint(5, 27))  # заповнюємо список температур рандомом
print(temperatures)
for temp in temperatures:
    if temp > swimming_temp:  # порівнюємо температури з температурою для плавання (вводить користувач)
        count += 1  # додаємо до лічильника 1, якщо знайдено
        continue
print(f"Температура була придатна для купання {count} рази")
