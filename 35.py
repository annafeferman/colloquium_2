"""Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим
за спаданням.
Anna Feferman"""

array = [] # порожній масив
flag = False # флаг, що покаже, чи знайдено елемент, більший за попередній
for i in range(int(input('Введіть довжину масиву: '))):
    array.append(int(input(f'Введіть {i+1} елемент: '))) # користувач самостійно заповнює масив
print(array)
for index in range(1, len(array)):
    if array[index] < array[index - 1]: # перевіряємо, чи кожний наступний елемент менше за попередній
        continue
    else:
        flag = True # якщо ні, змінюємо значення прапорця на true
if flag:
    print('No')
else:
    print('Yes')