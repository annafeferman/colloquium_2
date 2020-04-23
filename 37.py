"""Розсортуйте заданий лінійний масив по зростанню.
Anna Feferman"""


array = []
for i in range(int(input('Введіть довжину масиву: '))):
    array.append(int(input(f'Введіть {i+1} елемент: ')))


def bubble_sort(my_list): # використаємо бульбашковий алгоритм сортування
    last_item = len(my_list) - 1
    for k in range(last_item):  # вкладенним циклом перебираємо всі елементи масиву
        for j in range(last_item - k):
            if my_list[j] > my_list[j + 1]:  # кожен елемент, що менше за наступний, змінюємо з ним місцями
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

    return my_list


print(f'Вихідний список: {array}')
print(f'Відсортований список: {bubble_sort(array)}')