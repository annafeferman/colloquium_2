"""У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
Anna Feferman"""

from random import randint # імпортуємо рандом

array = []  # порожній список
count = 0
for i in range(30):
    array.append(randint(2, 7))  # заповнюємо рандінтом
print('Old: ', array)
j = 1
flag = False  # ставимо флаг
for i in range(30):
    while not flag:
        array[i + j - 1], array[i - j] = array[i - j], array[
            i + j - 1]  # змінюємо місцями елементи з відповідними індексами
        j += 1
        if array[i + j - 1] == array[i - j]:  # закінчуємо цикл, коли доходимо до центрального елемента
            flag = True
for el in array:
    if el > 5: # рахуємо де більше 5 мешканців
        count += 1
print('New: ', array)
print('> 5: ', count)
