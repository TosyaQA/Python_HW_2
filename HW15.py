# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

x = int(input("Введите число: "))
factorial = lambda x: ((x == 1) and 1) or x * factorial(x-1)
list2 = list( factorial(i) for i in range(1, x + 1))
print(list2)