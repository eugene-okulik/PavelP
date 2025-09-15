# Задача по обработке чисел
# Условие - Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь/

right_triangle_leg_1 = int(input("Введите значение катета_1: "))
right_triangle_leg_2 = int(input("Введите значение катета_2: "))
hypotenuse_right_triangle = (right_triangle_leg_1**2 + right_triangle_leg_2**2) ** 0.5
area_right_triangle = (right_triangle_leg_1 * right_triangle_leg_2) / 2

print(f"Гипотенуза прямоугольного треугольника: {hypotenuse_right_triangle}")
print(f"Площадь прямоугольного треугольника: {area_right_triangle}")
