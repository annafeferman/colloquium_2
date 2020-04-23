"""Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які
починаються з певної букви, яка вводиться з клавіатури.
Anna Feferman"""

letter = input('Input letter: ')  # користувач вводить літеру
surnames = ['Stendal', 'Bulgakov', 'Tolstoy', 'Azymov', 'Bronte']  # створюємо список з прізвищами
for surname in surnames:
    if surname[0] == letter: # порівнюємо першу літеру кожного прізвища з введенною
        print(surname) # друкуємо у разі співпадіння
    else:
        print('No such surnames')
        break