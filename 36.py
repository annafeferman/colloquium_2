"""Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
Anna Feferman"""

array = []  # створюємо порожній масив
summa = 0  # заводимо змінну для суми
for i in range(10):
    array.append(int(input(f'Input {i+1} element: ')))  # заповнюємо масив елементами вручну
for el in array:
    if el > 0:  # перевіряємо, чи число додатнє
        summa += el  # якщо так, додаємо до змінної суми
        continue
print(f'Сума: {summa}')  # виводимо результат
