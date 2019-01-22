__author__ = "Гонцов Александр Евгеньевич"

# Задание-1, EASY:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

number = input("Введите число ")
p = int(input("До какого знака вы хотите округлить число? "))

def round_number(number, p):
	rest_part = number - int(number)
	w = rest_part * (p * 10)
	working = w - int(w)
	if working >= 0,5:
		w + 1
	w / (10 * p)
	result = number + w
	return result

def round_number
input()

# Задание-2, EASY:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

ticket_number = list(input("Введите номер билета для проверки "))
print ("Номер билета", ticket_number)

def lucky(ticket_number):
	p = int(ticket_number[0] + ticket_number [1])
	q = int(ticket_number[4] + ticket_number [5])
	if p == q:
		print ("Билет счастливый, поздравляем!")
	else: print ("Хм, не в этот раз")

def lucky
input()

__author__ = "Гонцов Александр Евгеньевич"

# Задание-1, NORMAL:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

import math

def fibfun(n, m):

    fib_series = []
    a = 0
    w = 1
    for i in range(m):
        fib.append(w)
        a = w
        w = a+w
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    return res

n = int(imput("Введите n-элемент"))
m = int(imput("Введите m-элемент"))

fibfun(n, m)
input()

# Задача-2, NORMAL:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_list(given_list):
	def min_num(li):
        minimum = float('inf')
        for i in list1:
            if i < min_elem:
                min_elem = i
        return min_elem
    doing_list = [x for x in given_list]
    done_list = []
    while len(doing_list):
        for index in doing_list:
            if index == min_num(doing_list):
                done_list.append(index)
                doing_list.remove(index)
    del doing_list
    return done_list

sort_list([1, 2 , 5, 90, -67, 305, -6])
print(f"Элементы вашего списока: {given_list} отсортированны от минимального к максимальному: {done_list}")
input()