"""У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
Anna Feferman"""

from random import randint  # імпортуємо рандом

array = []  # масив порожній
for i in range(15):
    array.append(randint(10, 30))  # заповнюємо список рандомом від 10 до 30
print(array)
max_index = array.index(max(array)) # знаходимо індекс максимального елемента
array_2 = array[max_index:len(array)] # частина списку після максимального значення
array_3 = array[0: max_index+1] # частина списку до максимального значення
array_3.append(max_index) # додаємо індекс максимального елемента у першу частину списку
array_3.extend(array_2) # додаємо другу частину списку
print(array_3)
