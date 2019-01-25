__author__ = "Гонцов Александр Евгеньевич"

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

list1 = ["Banana", "Apple", "Mango", "Orange", "Kiwi", "Apricot", "Avocado", "Passion Fruit"]
list2 = ["Banana", "Carambola", "Mango", "Clementine", "Kiwi", "Papaya", "Passion Fruit"]
print ("Here is the first fruit list: ", list1)
print()
print ("Here is the second fruit list: ", list2)
print()

needed_list = list(x for x in list1 if x in list2)

print("There are fruits, which can be found in both lists: ", needed_list)
input()
         
