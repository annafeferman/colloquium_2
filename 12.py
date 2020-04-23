"""Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
Anna Feferman"""

from random import randint  # імпортуємо рандом

temperatures = []  # масив з температурами
count = 0  # лічильник
for temperature in range(10):  # 10 оскільки "декада"
    temperatures.append(randint(-20, 2))  # заповнюємо список температур рандомом
print(temperatures)
middle_temp = sum(temperatures)/len(temperatures) # знаходимо середню температуру
print(middle_temp)
for temp in temperatures:
    if temp > middle_temp:  # порівнюємо температури із середнім значенням
        count += 1  # додаємо до лічильника 1, якщо знайдено
        continue
print(f"Температура була вище середньої {count} рази")