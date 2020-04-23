"""З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
Anna Feferman"""

from random import randint  # імпортуємо рандом

temperatures = []
for temperature in range(13):
    temperatures.append(randint(-8, 22))  # заповнюємо список температур рандомом
descending = list(reversed(sorted(temperatures)))  # сортуємо і розвертаємо список (вказано, що темп-ра спадає)
print(descending)
for i in range(len(descending)):
    if descending[i] < 0:  # проходимо поелементно і шукаємо від'ємну темп-ру
        print(i + 8)  # додаємо 8, оскільки відлік часу починається з 8 годин
        break
