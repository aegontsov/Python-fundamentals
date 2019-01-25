__author__ = "Гонцов Александр Евгеньевич"

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

list1 = [random.randint (-100, 100) for i in range (30)]
print ("Your new list is formed: ", list1)
print()
needed_list = list(x for x in list1 if x % 3 == 0 and x > 0 and x % 4 != 0)
print("The list has been modified: ", needed_list)
input()
