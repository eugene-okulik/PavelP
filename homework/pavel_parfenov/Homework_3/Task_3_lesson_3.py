# Задача по обработке чисел
# Условие - Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

from math import sqrt

number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))
list_of_numbers = [number_a, number_b]
arithmetic_mean = sum(list_of_numbers) / len(list_of_numbers)
geometric_mean = sqrt(number_a * number_b)

print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Среднее геометрическое: {geometric_mean}")
