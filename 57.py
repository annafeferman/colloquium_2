"""Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
Anna Feferman"""

# у рядках 10-12 масиви з: зарплатою, працівниками, масив для пошуку найменш відмінного від середнього значення
wages = []
workers = []
diff_wages = []
for i in range(int(input('Input number of workers: '))):  # заповнюємо масиви власноруч
    workers.append(input('Input surname: '))
    wages.append(int(input('Input wages: ')))
table = dict(zip(workers, wages))  # об'єднуємо в словник
print('Таблиця: ', table)  # виводимо таблицю
middle_wages = sum(wages) / len(wages)  # рахуємо середню зарплатню
print(middle_wages)

for salary in wages:
    diff_wages.append(abs(middle_wages - salary))  # знаходимо різницю з середнім значенням

min_diff = min(diff_wages)  # знаходимо найменшу різницю
min_diff_index = diff_wages.index(min_diff)  # індекс, щоб знайти працівника
print('Зарплата відхиляється від середнього значення найменше у працівника ', workers[min_diff_index])

wages_sorted = sorted(wages)  # сортуємо, щоб знайти найбільшу зарплатню
print(f'Найбільша зарплатня у {workers[wages.index(wages_sorted[-1])]} i {workers[wages.index(wages_sorted[-2])]}')
print(f'Найбільша зарплатня у {workers[wages.index(wages_sorted[0])]}')
table.pop(workers[wages.index(wages_sorted[0])])  # видаляємо інформацію про працівника з найменшою зарплатнею
print(f'Оновлена таблиця: {table}')
