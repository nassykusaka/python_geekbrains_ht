# -*- coding: utf-8 -*-
import math

# normal: Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа
number = input("Пожалуйста, введите число: ")
digits = []
for i in range(len(number)):
    digits.append(int(number[i]))
print(max(digits))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные
a = int(input("Введите значение для а:"))
b = int(input("Введите значение для b:"))
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.

def quadratic(a, b, c):
	if (b**2 - 4*a*c) >0:
		x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
		x2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
	else:
		print('there is no x')
    return(x1, x2)

# hard: Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True
# Вопрос: Чему была равна переменная a, если точно известно что её значение не изменялось?