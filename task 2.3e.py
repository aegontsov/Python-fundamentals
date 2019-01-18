__author__ = "Гонцов Александр Евгеньевич"

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

num_list = [1, 3, 5, 7, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
changed_list = []

print("Here is the list of numbers: ", num_list)

for i in num_list:
	if i % 2 == 0:
        ni = i / 4
        changed_list.append(ni)
        num_list.remove(i) 
	else: i = i * 2
		changed_list.append(i)
print("Here is the new list. Can you guess the rule of change? ", changed_list)

input()

