__author__ = "Гонцов Александр Евгеньевич"

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruits_list = ["banana", "watermelon", "pineapple", "lime", "mango"]

for i, value in enumerate(fruits_list, 1):
	print("{}. {:>20}".format(i, value))

input()
