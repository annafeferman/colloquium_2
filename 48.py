"""Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
Anna Feferman"""

array = []  # порожній список
for i in range(int(input('Input number: '))):
    array.append(input('Input surname: '))  # вводимо прізвища
print('Old list: ', array)
j = 1
flag = False  # ставимо флаг
for i in range(len(array)):
    while not flag:
        array[i + j - 1], array[i - j] = array[i - j], array[
            i + j - 1]  # змінюємо місцями елементи з відповідними індексами
        j += 1
        if array[i + j - 1] == array[i - j]:  # закінчуємо цикл, коли доходимо до центрального елемента
            flag = True
print('New list: ', array)
