# Задача по обработке чисел
# Условие - Даны числа x и y. Получить x − y / 1 + xy

number_x = int(input("Введите число x: "))
number_y = int(input("Введите число y: "))

print(f"Результат: {number_x-number_y/1+number_x*number_y}")
