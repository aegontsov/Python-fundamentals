import random


class Card:
	def __init__(self, name):
		bag = [x for x in range(1, 91)]  
		self.card = [
		    __class__.gen_string(bag),
		    __class__.gen_string(bag),
		    __class__.gen_string(bag)
		]
		self.name = name
		self.count_barrel = 15  

	@staticmethod
	def gen_string(bag):
		string = ['' for _ in range(9)]
		for x in range(8, 3, -1):
			digit = random.randint(0, x)  
			while string[digit] != '':  
				digit += 1
			string[digit] = bag.pop(random.randint(0, len(bag) - 1))
		return string

	def __str__(self):
		rez = '{:-^26}\n'.format(self.name)
		for x in range(3):
			rez += '{:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2} {:>2}'\
                    .format(*self.card[x]) + '\n'
		return rez + '--------------------------'


player = Card(' Ваша карточка ')
computer = Card(' Карточка компьютера ')

bag = [x for x in range(1, 91)]  
while True:
	if len(bag) < 1:
		print('Все бочонки разыграны. Результаты игры:\n'
		      'У компьютера не зачтено {} числа,\n'
		      'у вас не зачтено {} числа.'.format(
		          computer.count_barrel, player.count_barrel))
		break
	barrel = bag.pop(random.randint(0, len(bag) - 1))
	print('\nВыпал бочонок: {} (В мешке осталось {} штук)'.format(barrel, len(bag)))
	print(computer)
	print(player)
	reply = input('Зачеркнуть цифру в карточке? (+ или - или quit)\n')
	reply = reply.lower()
	while len(reply) == 0:
		print('\n\nСимвол не известен\n')
		print('Выпал бочонок: {} (В мешке осталось {} штук)'.format(barrel, len(bag)))
		print(computer)
		print(player)
		reply = input('Зачеркнуть цифру в карточке? (+ или - или quit)\n')
		reply = reply.lower()

	if reply == 'quit':
		print('Вы вышли из игры')
		break
	elif reply == '+':
		test = False 
		for x in range(3):
			if barrel in player.card[x]:
				test = True
				player.card[x][player.card[x].index(barrel)] = '-'
				player.count_barrel -= 1
			if barrel in computer.card[x]:
				computer.card[x][computer.card[x].index(barrel)] = '-'
				computer.count_barrel -= 1
		if test:
			if player.count_barrel < 1:
				print('Вы победили!')
				break
			elif computer.count_barrel < 1:
				print('Компьютер победил!')
				break
		else:
			print('В вашей карточке нет такого числа. Вы проиграли, в следующий раз будьте внимательнее!')
			break
	elif reply == '-':
		test = False
		for x in range(3):
			if barrel in player.card[x]:
				print('В вашей карточке есть такое число. Вы проиграли, в следующий раз будьте внимательнее!')
				test = True
				break
			if barrel in computer.card[x]:
				computer.card[x][computer.card[x].index(barrel)] = '-'
				computer.count_barrel -= 1
		if test:
			break
		if player.count_barrel < 1:
			print('Вы победили!')
			break
		elif computer.count_barrel < 1:
			print('Компьютер победил!')
			break
