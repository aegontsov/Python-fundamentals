__author__ = "Гонцов Александр Евгеньевич"

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print("Welcome!")
age = int(input("How old are you? "))

if age >= 18:
	print("Access is allowed")
else:
	print("Sorry, access is forbidden")

input()