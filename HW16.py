# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

# Пример:
# -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

n = int(input())
lst = [round((1+1/n)**n, 3)
for n in range(1, n+1)]
print(f"Последовательность: {lst}\nСумма: {round(sum(lst), 3)}")