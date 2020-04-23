"""Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.
Anna Feferman"""

surnames = ['Stendal', 'Bulgakov', 'Tolstoy', 'Azymov', 'Fadeev'] # створюємо список з прізвищами
reversed_surnames = surnames[::-1] # розвертаємо його за допомогою зрізу
for surname in reversed_surnames:
    print(surname) # проходимо по ньому циклом for

